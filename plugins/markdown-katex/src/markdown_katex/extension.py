# This file is part of the markdown-katex project
# https://gitlab.com/mbarkhau/markdown-katex
#
# Copyright (c) 2019 Manuel Barkhau (mbarkhau@gmail.com) - MIT License
# SPDX-License-Identifier: MIT
import re
import json
import base64
import typing as typ
import hashlib
import logging

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor

import markdown_katex.wrapper as wrapper

log = logging.getLogger(__name__)


SVG_ELEM_RE = re.compile(r"<svg.*?</svg>", flags=re.MULTILINE | re.DOTALL)

SVG_XMLNS = 'xmlns="http://www.w3.org/2000/svg" ' + 'xmlns:xlink="http://www.w3.org/1999/xlink" '

KATEX_STYLES = """
<link rel="stylesheet"
    href="https://cdn.jsdelivr.net/npm/katex@0.10.2/dist/katex.css"
    integrity="sha256-SSjvSe9BDSZMUczwnbB1ywCyIk2XaNly9nn6yRm6WJo="
    crossorigin="anonymous" />
<style type="text/css">
    .katex img {
      display: block;
      position: absolute;
      width: 100%;
      height: inherit;
    }
</style>
"""


B64IMG_TMPL = '<img src="data:image/svg+xml;base64,{img_text}"/>'


def make_marker_id(text: str) -> str:
    data = text.encode("utf-8")
    return hashlib.md5(data).hexdigest()


def svg2img(html: str) -> str:
    """Converts inline svg elements to images.

    This is done as a work around for #75 of WeasyPrint
    https://github.com/Kozea/WeasyPrint/issues/75
    """
    while True:
        match = SVG_ELEM_RE.search(html)
        if match:
            svg_text = match.group(0)
            if "xmlns" not in svg_text:
                svg_text = svg_text.replace("<svg ", "<svg " + SVG_XMLNS)
            svg_data = svg_text.encode("utf-8")
            img_b64_data: bytes = base64.standard_b64encode(svg_data)
            img_b64_text = img_b64_data.decode("utf-8")
            img_b64_tag  = B64IMG_TMPL.format(img_text=img_b64_text)
            start, end = match.span()
            html = html[:start] + img_b64_tag + html[end:]
        else:
            break

    return html


def _clean_block_text(block_text: str) -> str:
    if block_text.strip().startswith("```math"):
        block_text = block_text[len("```math") :]
    elif block_text.strip().startswith("~~~math"):
        block_text = block_text[len("~~~math") :]

    if block_text.strip().endswith("```"):
        block_text = block_text[: -len("```")]
    elif block_text.strip().endswith("~~~"):
        block_text = block_text[: -len("~~~")]
    return block_text


def tex2html(tex: str, options: wrapper.Options = None) -> str:
    if options:
        no_inline_svg = options.get("no_inline_svg", False)
    else:
        no_inline_svg = False

    # These are options of the extension, not of the katex-cli program.
    if options:
        options.pop('no_inline_svg'   , None)
        options.pop('insert_fonts_css', None)

    result = wrapper.tex2html(tex, options)
    if no_inline_svg:
        result = svg2img(result)
    return result


def md_block2html(block_text: str, default_options: wrapper.Options = None) -> str:
    options: wrapper.Options = {'display-mode': True}

    if default_options:
        options.update(default_options)

    block_text = _clean_block_text(block_text)
    header, rest = block_text.split("\n", 1)
    if "{" in header and "}" in header:
        options.update(json.loads(header))
        block_text = rest

    return tex2html(block_text, options)


def _clean_inline_text(inline_text: str) -> str:
    if inline_text.startswith("$``"):
        inline_text = inline_text[len("$``") :]
    if inline_text.startswith("$`"):
        inline_text = inline_text[len("$`") :]
    if inline_text.endswith("``$"):
        inline_text = inline_text[: -len("``$")]
    if inline_text.endswith("`$"):
        inline_text = inline_text[: -len("`$")]
    return inline_text


def md_inline2html(inline_text: str, default_options: wrapper.Options = None) -> str:
    options     = default_options.copy() if default_options else {}
    inline_text = _clean_inline_text(inline_text)
    return tex2html(inline_text, options)


INLINE_DELIM_RE = re.compile(r"`{1,2}")


class InlineCodeItem(typ.NamedTuple):

    inline_text   : str
    marker        : str
    rewritten_line: str


def iter_inline_katex(line: str) -> typ.Iterable[InlineCodeItem]:
    pos = 0
    while True:
        inline_match_start = INLINE_DELIM_RE.search(line, pos)
        if inline_match_start is None:
            break

        pos   = inline_match_start.end()
        start = inline_match_start.start()
        delim = inline_match_start.group()

        try:
            end = line.index(delim, start + len(delim)) + (len(delim) - 1)
        except ValueError:
            continue

        pos = end

        if line[start - 1] != "$":
            continue
        if line[end + 1] != "$":
            continue

        inline_text = line[start - 1 : end + 2]
        marker_id   = make_marker_id("inline" + inline_text)
        marker      = f"<span id='katex{marker_id}'>katex{marker_id}</span>"
        line        = line[: start - 1] + marker + line[end + 2 :]

        pos = end + len(delim) - len(inline_text) + len(marker)

        yield InlineCodeItem(inline_text, marker, line)


class KatexExtension(Extension):
    def __init__(self, **kwargs) -> None:
        self.config = {
            'no_inline_svg'   : ["", "Replace inline <svg> with <img> tags."],
            'insert_fonts_css': ["", "Insert font loading stylesheet."],
        }
        for name, options_text in wrapper.parse_options().items():
            self.config[name] = ["", options_text]

        self.options: wrapper.Options = {}
        for name in self.config.keys():
            if name in kwargs:
                val = kwargs[name]
            else:
                val = self.getConfig(name, "")

            if val != "":
                self.options[name] = val

        self.math_html: typ.Dict[str, str] = {}
        super(KatexExtension, self).__init__(**kwargs)

    def reset(self) -> None:
        self.math_html.clear()

    def extendMarkdown(self, md, *args, **kwargs) -> None:
        preproc = KatexPreprocessor(md, self)
        md.preprocessors.register(preproc, name='katex_fenced_code_block', priority=50)

        postproc = KatexPostprocessor(md, self)
        md.postprocessors.register(postproc, name='katex_fenced_code_block', priority=0)
        md.registerExtension(self)


FENCE_RE      = re.compile(r"^(\s*)(```|~~~)")
MATH_FENCE_RE = re.compile(r"^(\s*)(```|~~~)math")


class KatexPreprocessor(Preprocessor):
    def __init__(self, md, ext: KatexExtension) -> None:
        super(KatexPreprocessor, self).__init__(md)
        self.ext: KatexExtension = ext

    def run(self, lines: typ.List[str]) -> typ.List[str]:
        is_in_math_fence     = False
        is_in_fence          = False
        expected_close_fence = "```"
        block_prefix         = ""

        block_lines: typ.List[str] = []
        out_lines  : typ.List[str] = []

        for line in lines:
            if is_in_fence:
                out_lines.append(line)
                is_ending_fence = line.strip() == expected_close_fence
                if is_ending_fence:
                    is_in_fence = False
            elif is_in_math_fence:
                block_lines.append(line.lstrip())
                is_ending_fence = line.strip() == expected_close_fence
                if not is_ending_fence:
                    continue

                is_in_math_fence = False
                block_text       = "\n".join(block_lines).rstrip()
                del block_lines[:]
                math_html = md_block2html(block_text, self.ext.options)
                marker_id = make_marker_id("block" + block_text)
                marker    = f"<p id='katex{marker_id}'>katex{marker_id}</p>"
                tag_text  = f"<p>{math_html}</p>"
                out_lines.append(f"{block_prefix}{marker}")
                self.ext.math_html[marker] = tag_text
            else:
                math_fence_match = MATH_FENCE_RE.match(line)
                fence_match      = FENCE_RE.match(line)
                if math_fence_match:
                    is_in_math_fence     = True
                    block_prefix         = math_fence_match.group(1)
                    expected_close_fence = math_fence_match.group(2)
                    block_lines.append(line.lstrip())
                elif fence_match:
                    is_in_fence          = True
                    expected_close_fence = fence_match.group(2)
                    block_lines.append(line)
                else:
                    for inline_code in iter_inline_katex(line):
                        math_html = md_inline2html(inline_code.inline_text, self.ext.options)
                        self.ext.math_html[inline_code.marker] = math_html
                        line = inline_code.rewritten_line

                    out_lines.append(line)

        return out_lines


# NOTE (mb):
#   Q: Why this business with the Postprocessor? Why
#   not just do `out_lines.append(tag_text)` and save
#   the hassle of `self.ext.math_html[marker] = tag_text` ?
#   A: Maybe there are other processors that can't be
#   trusted to leave the inserted markup alone. Maybe
#   the inserted markup could be incorrectly parsed as
#   valid markdown.


class KatexPostprocessor(Postprocessor):
    def __init__(self, md, ext: KatexExtension) -> None:
        super(KatexPostprocessor, self).__init__(md)
        self.ext: KatexExtension = ext

    def run(self, text: str) -> str:
        if not any(marker in text for marker in self.ext.math_html):
            return text

        if self.ext.options:
            insert_fonts_css = self.ext.options.get("insert_fonts_css", True)
        else:
            insert_fonts_css = True

        if insert_fonts_css and KATEX_STYLES not in text:
            text = KATEX_STYLES + text

        for marker, html in self.ext.math_html.items():
            wrapped_marker = "<p>" + marker + "</p>"
            if wrapped_marker in text:
                text = text.replace(wrapped_marker, html)
            elif marker in text:
                text = text.replace(marker, html)
            else:
                log.warning(f"KatexPostprocessor couldn't find: {marker}")

        return text
