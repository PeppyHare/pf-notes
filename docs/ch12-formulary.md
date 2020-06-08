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
    \quad \rightarrow \quad 
    ```
    ```math
    \text{Energy:} \qquad 
    ```

## Ideal MHD

!!! info "Conservation Law Form of Ideal MHD"

    ```math
    \pdv{\rho}{t} + \div (\rho \vec v) = 0
    ```
    ```math
    \pdv{(\rho \vec v)}{t} + \div \left[ \rho \vec v \vec v - \frac{\vec B \vec B}{\mu_0} + \left( p + \frac{B^2}{2 \mu_0} \right) \overline{I} \right] = 0
    ```
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
    
    ```
    