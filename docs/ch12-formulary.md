# Formulary

!!! info "Kinetic Description"

    ```math
    \dv{\vec v}{t} = \frac{q_i}{m_i} (\vec E + \vec v_i \cross \vec B) + \sum_{j \neq i} \left[ \left. \dv{\vec v_{ij}}{t} \right|_{coll} \delta(\vec r_i - \vec r_j) \right]
    ```
    ```math
    \pdv{\vec B}{t} = - \curl \vec E
    ```
    ```math
    \frac{1}{c^2} \pdv{\vec E}{t} = \curl \vec B - \mu_0 \sum_i q_i \vec v_i \delta (\vec r - \vec r_i)
    ```
    ```math
    \div \vec B = 0
    ```
    ```math
    \div \vec E = \frac{1}{\epsilon_0} \sum_i q_i \delta (\vec r - \vec r_i)
    ```
    Klimontovich equation:
    ```math
    \dv{N}{t} = 0 = \pdv{N}{t} + \pdv{}{q_i} \cdot (\dot{q_i} N) \\
    N \equiv \sum_i \delta (p - p_i) \delta(q - q_i)
    ```

!!! info "Plasma Fluid Description"
    
    Boltzmann Equation
    ```math
    \pdv{f_\alpha}{t} + \vec v \cdot \pdv{f_\alpha}{t} + \frac{q_\alpha}{m_\alpha} (\vec E + \vec v \cross \vec B) \cdot \pdv{f_\alpha}{\vec v} = \left. \pdv{f_\alpha}{t} \right|_{coll} = \sum_{\beta \neq \alpha} C_{\alpha \beta}
    ```
    
    Maxwellian distribution:
    ```math
    f_\alpha (\vec v) = n_\alpha \left( \frac{m_\alpha}{2 \pi T} \right)^{3/2} e^{- \frac{m_\alpha(\vec v - \vec v_\alpha)^2}{2T}}
    ```
    Moments of fluid model (moments of distribution $` \rightarrow `$ moments of Boltzmann equation:
    ```math
    \text{Continuity:} \qquad n_\alpha = \int f_\alpha \dd \vec v \\
    \quad \rightarrow \pdv{n_\alpha}{t} + \div (n_\alpha \vec v_\alpha) = 0
    ```
    ```math
    \text{Momentum:} \qquad n_\alpha \vec v_\alpha = \int \vec v f_\alpha \dd v \\
    \quad \rightarrow \quad \pdv{}{t} (n_\alpha \vec v_\alpha ) + \div (n_\alpha \vec v_\alpha \vec v_\alpha) + \frac{1}{m_\alpha} \div \vec P_\alpha - \frac{q_\alpha}{m_\alpha} n_\alpha ( \vec E + \vec v _\alpha \cross \vec B) = \sum_{\beta \neq \alpha} \int \vec w C_{\alpha \beta} \dd \vec v
    ```
    ```math
    \rightarrow \rho_\alpha \left(\pdv{\vec v_\alpha}{t} + \vec v_\alpha \cdot \grad \vec v_\alpha \right) + \grad \vec P_\alpha + \div \vec \Pi_\alpha - q_\alpha n_\alpha (\vec E + \vec v_\alpha \cross \vec B) = \sum_{\beta \neq \alpha} \vec R_{\alpha \beta}
    ```
    ```math
    \text{Energy:} \qquad \int \vec v \vec v \pdv{f_\alpha}{t} \dd \vec v = \pdv{}{t} \int \vec v \vec v f_\alpha \dd \vec v = \pdv{}{t} \vec E_\alpha / m_\alpha \rightarrow \pdv{}{t} \vec P_\alpha
    ```
    ```math
    \rightarrow \quad \frac{3}{2} n_\alpha \left( \pdv{T_\alpha}{t} + \vec v_\alpha \cdot \grad T_\alpha \right) + P_\alpha \div \vec v_\alpha + \vec \Pi_\alpha \cdot \cdot \grad \vec v_\alpha + \div \vec h_\alpha = \sum_{\beta \neq \alpha} Q_{\alpha \beta}
    ```
    Closure relations
    ```math
    \vec h_\alpha = - \kappa \grad T_\alpha
    ```
    ```math
    \overline \Pi_ \alpha = \nu \grad \vec v_\alpha
    ```

## Ideal MHD

!!! info "Ideal MHD"

    Continuity:
    ```math
    \pdv{\rho}{t} + \div (\rho \vec v) = 0
    ```
    Momentum:
    ```math
    \rho \left( \pdv{\vec v}{t} + \vec v \cdot \grad \vec v \right) + \grad p - \vec j \cross \vec B = 0
    ```
    Generalized Ohm's Law
    ```math
    \vec E + \vec v \cross \vec B = \frac{1}{Zen}\cancel{(\vec j \cross \vec B - \grad p_e)} = 0
    ```
    Energy
    ```math
    \dv{}{t} \left( \frac{p}{\rho^\gamma} \right) = 0
    ```

!!! info "Lawson Criterion"

    ```math
    n \tau_E > 10^4 s/m^3
    ```


!!! info "Conservation Law Form of Ideal MHD"

    Continuity:
    ```math
    \pdv{\rho}{t} + \div (\rho \vec v) = 0
    ```
    Momentum:
    ```math
    \pdv{(\rho \vec v)}{t} + \div \left[ \rho \vec v \vec v - \frac{\vec B \vec B}{\mu_0} + \left( p + \frac{B^2}{2 \mu_0} \right) \overline{I} \right] = 0
    ```
    Energy:
    ```math
    \pdv{\epsilon}{t} + \div \left[ \left( \epsilon + p + \frac{B^2}{2 \mu_0} \right) \vec v - (\vec B \cdot \vec v) \frac{\vec B}{\mu_0} \right] = 0
    ```
    ```math
    \pdv{\vec B}{t} + \div ( \vec v \vec B - \vec B \vec v) = 0
    ```
    where
    ```math
    \epsilon = \frac{1}{\gamma - 1} p + \frac{1}{2} \rho v^2 + \frac{B^2}{2\mu_0}
    ```

    Static Equilibrium:
    ```math
    \vec j \cross \vec B = \grad p
    ```
    ```math
    \frac{B^2}{\mu_0} \vec K = \grad_\perp (p + \frac{B^2}{2 \mu_0})
    ```
    ```math
    \vec K \equiv \frac{\vec B}{|B|} \cdot \grad \frac{ \vec B}{|B|}
    ```

    Conservation of flux:
    ```math
    \vec E + \vec v \cross \vec B = 0
    ```
    ```math
    \pdv{\vec B}{t} = - \curl \vec E
    ```
    ```math
    \rightarrow \dv{}{t} \left( \frac{\vec B}{\rho} \right) = \frac{\vec B}{\rho} \cdot \grad \vec v
    ```

## 1D Equilibria

!!! info "$` \theta `$-pinch"

    ```math
    B_\theta = 0
    ```
    ```math
    j_\theta B_z = \dv{p}{r}
    ```
    ```math
    j_\theta = - \frac{1}{\mu_0} \dv{B_z}{r}
    ```
    ```math
    \rightarrow p + \frac{B_z ^2}{2 \mu_0} = \frac{B_0 ^2}{2 \mu_0}
    ```
    ```math
    \langle \beta \rangle = \frac{2}{a^2} \int_0 ^a \frac{r p}{B_0 ^2 / 2 \mu_0} \dd r
    ```
    ```math
    q = \infty
    ```
    ```math
    W = \frac{\mu_0 r}{B_z ^2} \dv{}{r} \left( p + \frac{B_z ^2}{2 \mu_0} \right) = 0
    ```

!!! info "Z-pinch"

    ```math
    B_z =0
    ```
    ```math
    \grad p = \dv{p}{r} = - j_z B_\theta
    ```
    ```math
    - \dv{}{r} \left( p + \frac{B_\theta ^2}{2 \mu_0} \right) = \frac{B_\theta ^2}{\mu_0 r}
    ```
    ```math
    \langle \beta \rangle = \frac{2 \mu_0}{B_0 ^2 \pi a^2} \int _0 ^a 2 \pi r p \dd r = 1 \quad \text{ if } \quad p(a) = 0
    ```
    ```math
    q = S = 0
    ```
    ```math
    W = 1
    ```

!!! info "Screw pinch"

    ```math
    \dv{}{r} \left( p + \frac{B^2}{2 \mu_0} \right) = - \frac{B_\theta ^2}{\mu_0 r}
    ```
    ```math
    \beta_t = \frac{2 \mu_0}{B_z (a) ^2} \left( \frac{1}{\pi a^2} \int_0 ^a 2 \pi r p \dd r \right)
    ```
    ```math
    \beta_p = \left( 1 - \frac{\alpha_t}{\beta _t} \right)^{-1} \qquad \alpha_t \equiv \frac{2}{a^2} \int_0 ^a \left(1 - \frac{B_z ^2}{B_0 ^2} \right) r \dd r
    ```
    ```math
    q = \frac{2 \pi r B_z}{L B_\theta}
    ```
    ```math
    q_a = \frac{4 \pi ^2 a^2 B_0}{\mu_0 I_a}
    ```
    ```math
    S = \frac{r}{q} \dv{q}{r}
    ```
    ```math
    W = - \frac{B_\theta ^2}{B_\theta ^2 + B_z ^2}
    ```

!!! info "Stability"

    Shear:
    ```math
    S = 2 \frac{ dq / q}{dV / V} = 2 \frac{d \ln q}{d \ln V}
    ```
    ```math
    q = \frac{\text{\# long windings}}{\text{\# short windings}} = \dv{\psi_t}{\psi_p}
    ```
    Shear for toroid
    ```math
    q = \frac{r B_\phi}{R B_\theta}
    ```
    Shear for cylinder
    ```math
    q = 2 \pi \frac{r B_z}{L B_\theta}
    ```
    Well
    ```math
    W = \frac{ d \langle p + B^2 / 2 \mu_0 \rangle / \langle B^2 / 2 \mu_0 \rangle}{dV / V}
    ```
    For stabilization, $` B^2 / 2 \mu_0 `$ should increase faster than $` p `$ decreases

## 2D Equilibria

!!! info "Grad-Shafranov Equation: Static toroidal equilibrium"

    ```math
    \grad p = \vec j_\theta \cross \vec B_\phi + \vec j_\phi \cross \vec B_\theta
    ```
    ```math
    A_\phi = \frac{\phi}{R} \vu \phi
    ```
    ```math
    \phi = \frac{\phi_p}{2 \pi}
    ```
    ```math
    \vec B_\theta = - \frac{\vu R}{R} \pdv{\psi}{z} + \frac{ \vu z}{R} \pdv{\psi}{R} = \frac{ \grad \psi}{R} \cross \vu \phi
    ```
    ```math
    F \equiv R B_\phi
    ```
    ```math
    \Delta ^\star \equiv R \pdv{}{R} \frac{1}{R} \pdv{}{R} + \pdv{^2}{z^2}
    ```
    ```math
    \Delta ^\star \psi = \pdv{^2 \psi}{z^2} + \pdv{^2 \psi}{R^2} - \frac{1}{R} \pdv{\psi}{R}
    ```
    ```math
    \vec j_\phi = - \frac{1}{\mu_0 R} \Delta ^\star \psi \vu \phi
    ```
    ```math
    \vec j_\theta = \frac{1}{\mu_0 R} \grad (F) \cross \vu \phi
    ```
    ```math
    R^2 \mu_0 \pdv{p}{\psi} = - \Delta ^\star \psi - F \pdv{F}{\psi}
    ```
    ```math
    q(\psi) = \frac{F(\psi)}{2 \pi} \oint_{p} \frac{r \dd \theta}{R^2 B_\theta}
    ```
    Limits:
    ```math
    \text{Force-free:} \qquad \vec j \parallel \vec B
    ```
    ```math
    \rightarrow \Delta ^\star \psi + F F' = 0
    ```
    ```math
    \text{Connected $\theta$ pinch:} \qquad FF' \gg \Delta ^\star \psi
    ```
    ```math
    \rightarrow \grad p \approx \vec j_\theta \cross \vec B_\phi
    ```
    ```math
    \text{Connected Z-pinch:} \qquad FF' \ll \Delta ^\star \phi
    ```
    ```math
    \rightarrow \grad p \approx j_\phi \cross B_\theta
    ```

## MHD Stability

!!! info "Linear stability"
    
    ```math
    \pdv{\rho_1}{t} = - \vec v_1 \grad \rho_0 - \rho_0 \div \vec v_1
    ```
    ```math
    \pdv{\vec B_1}{t} = \curl ( \vec v_1 \cross \vec B_0)
    ```
    ```math
    \rho_0 \pdv{\vec v_1}{t} = - \grad p_1 + \vec j_0 \cross \vec B_1 - \vec j_1 \cross \vec B_0
    ```
    ```math
    \pdv{p_1}{t} = - \vec v_1 \cdot \grad p_0 - \gamma p_0 \div \vec v_1
    ```
    For linear perturbation $` \vec \xi = \int_0 ^t \vec v_1 \dd t `$ the momentum equation becomes
    ```math
    \rho_0 \pdv{^2 \xi}{t^2} = \vec F(\xi)
    ```
    where
    ```math
    F(\xi) = \grad (\xi \cdot \grad p_0 + \gamma p_0 \div \xi) + \frac{1}{\mu_0} \left[ ( \curl \vec B_0) \cross \curl (\xi \cross \vec B_0) + \curl \curl (\xi \cross \vec B_0) \cross \vec B_0 \right]
    ```
    Eigenvalues of $` \frac{1}{\rho_0} \vec F (\xi) = \omega^2 \xi `$ are real and ordered. Only need to check $` n=0 `$ to determine stability/instability of configuration.

!!! info "$` \delta W `$ Approach"

    $` \delta W = `$ change in potential energy due to a displacement $` \xi `$
    ```math
    \delta W < 0  \rightarrow \text{instability}
    ```
    ```math
    \delta W = - \frac{1}{2} \int \xi \cdot F(\xi) \dd V = \delta W_F + \delta W_S + \delta W_V
    ```
    Surface term:
    ```math
    \delta W_s = \frac{1}{2} \oint \dd S (\vu n \cdot \xi) ^2 \left( \vu n \cdot \grad p_0 + \left[ \vu n \cdot \grad \frac{B_0 ^2}{2 \mu_0} \right]_{jump} \right)
    ```
    Vacuum term:
    ```math
    \delta W_V = \int_{vac} \dd V \frac{B_1 ^2}{\mu_0}
    ```
    Plasma (free) term:
    ```math
    \delta W_F = \frac{1}{2} \int \dd V \frac{ |B_{1, \perp}|^2}{\mu_0} \quad \leftarrow \text{Shear Alfven} \\
    + \mu_0 \left| \frac{B_{1, \parallel}}{\mu_0}  - \frac{B_0 \xi \cdot \grad p_0}{B_0} ^2 \right|^2 \quad \leftarrow \text{Fast magnetosonic} \\
    + \Gamma p_0 |\div \xi|^2 \quad \leftarrow \text{Acoustic}\\
    + \frac{\vec j_0 \cdot \vec B_0}{B_0 ^2} (\vec B_0 \cross \vec \xi) \cdot \vec B_1  \quad \leftarrow \text{Current-driven (kink)}  \\
    - 2 ( \vec \xi \cdot \grad p_0)(\vec \xi \cdot \vec \kappa) \quad \leftarrow \text{pressure-driven (interchange/balooning)}
    ```
    Shear Alfven, fast magnetosonic, and acoustic modes are stabilizing. Current-driven and pressure-driven modes can lead to instability.
