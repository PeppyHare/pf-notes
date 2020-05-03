#!/bin/bash -ex

cd plugins/markdown-katex
python3 setup.py build
pip3 install --editable .
cd -