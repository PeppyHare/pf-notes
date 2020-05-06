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