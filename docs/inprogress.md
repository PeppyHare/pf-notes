

## Conservation Law Form of MHD

$$
\pdv{}{t} q + \div \vec f = 0
$$

We can express momentum in conservation law form:

$$
\pdv{}{t} (\rho \vec v) + \div \left[ \rho \vec v \vec v - \frac{ \vec B \vec B}{\mu_0} + (p + \frac{B^2}{2 \mu_0})\vec 1 \right] = 0
$$

The conservation law form for the magnetic field looks like

$$
\pdv{ \vec B}{t} + \div \left[ \vec v \vec B - \vec B \vec v \right ] = 0
$$

And of course the energy equation for

$$
E = \frac{1}{\gamma - 1} p + \frac{1}{2} \rho v^2 + \frac{ B^2}{2 \mu_0}
$$

$$
\pdv{E}{t} + \div \left[ \left( E + p + \frac{B^2}{2 \mu_0} \right) - \left( \frac{ \vec B \cdot \vec v}{\mu_0} \right) \vec B \right] = 0
$$

Conservation law forms are particularly useful when considering equilibrium steady-state force balance. This means that in steady-state equilibrium we have

$$
\div \left[ \rho \vec v \vec v - \frac{ \vec B \vec B}{\mu_0} + \left( p + \frac{B^2}{2 \mu_0} \right) \vec 1 \right] = 0
$$

We can use this relationship and integrate over various volumes to determine the relationship between the various force balance terms


Real-world example: ITER

 - \( \beta \) (normalized): 2%
 - length (cm): 600 (major radius) or 200 (minor radius)
 - n (particles/cm^3): \( 10^{14} \)
 - T (keV): 8

### Examples of equilibrium plasma confinement

For a plasma in static equilibrium \( \vec v = 0 \rightarrow \vec j \cross \vec B = \grad p \) 

$$
 \div \vec T = 0 = \div \left( \right) 
 $$

$$
\vec j \cross \vec B = \frac{1}{\mu_0} (\curl \vec B) \cross \vec B = \frac{1}{\mu_0} (\vec B \cdot \grad \vec B - \frac{1}{2} \grad B^2) \\
= \frac{1}{\mu_0} ( B^2 \vu e_B \cdot \grad \vu e_B + \frac{1}{2} \vu e_B \vu e_B \cdot \grad B^2 - \frac{\grad B^2}{2} )
$$

where \( \vu e_B = \vec B / B \) 

\( \vu e_B \cdot \grad \vu e_B \) is the curvature of \( \vec B \). Write it like a curvature

$$
\vec K = - \vu r / R_c
$$

$$
\vu e_B \vu e_B \cdot \grad B^2
$$
is gradient of \( B^2 \) that is parallel to B. Multiply by \( e_B \) gives the component of gradient along \( e_B \). The difference between that and \( \grad B^2 / 2 \) gives you the perpendicular gradient

$$
\vec j \cross \vec B = \frac{1}{\mu_0} (B^2 \vec \kappa - \frac{1}{2} \grad _\perp B^2) = \grad p = \grad_\perp p
$$

identify \( B^2 \vec \kappa \) is magnetic tension resulting from having a bent magnetic field line. \( \frac{1}{2} \grad_\perp B^2  \) is magnetic pressure. They have to balance the plasma pressure at equilibrium.

For example, consider a cylindrical plasma that's in equilibrium with a helical magnetic field
$$
\vec B = B_\theta (r) \vu \theta + B_z (r) \vu z
$$

How is plasma pressure profile determined by the different components of the magnetic field? If we want to maximize the amount of pressure we confine, what should be maximized/minimized?

$$
\frac{B^2}{\mu_0} \vu \kappa = \grad _\perp ( p + \frac{B^2}{2 \mu_0} ) 
$$

\( B_z \) is straight and has no curvature, so the only magnetic tension comes from \( B_\theta \), so the magnetic tension from \( B_\theta \) must balance the total pressure.

<p align="center"> <img alt="Figure 12.6" src="../img/12.6.png" /> </p>

The role of \( B_z \) is displacing plasma pressure. The utility in defining \( \beta \) as

$$
\beta = \frac{\text{plasma pressure}}{\text{magnetic pressure}}
$$

### Conditions of Ideal MHD Validity

The conditions for ideal MHD to be valid are

1. High Ion Collisionality: \( \frac{\tau_{ii}}{\tau} \ll 1 \) 
2. Small ion Larmor radius: \( \frac{r_{L, i}}{L} \ll 1 \) 
3. Low resistivity: \( \left(\frac{m_e}{m_i} \right)^{3/2} \left( \frac{r_{L, i}}{L} \right)^2 \ll 1 \) 

For a given plasma in force balance, we can relate the plasma pressure to the magnetic pressure

$$
\beta = \frac{n T}{B^2 / 2 \mu_0} = 4 \times 10^{-16} \frac{n_{cm^{-3}} T_{keV}}{B^2 _{T}}
$$

Ion collision time is (Spitzer collisionality)

$$
\tau_{ii} = 2.09 \times 10^{7} \frac{T_{eV} ^{3/2} \mu ^{1/2}}{\ln \Lambda n_{cm ^{-3}}} \left[\text{s}\right]
$$
where \( \mu \equiv m_i / m_p \).

Putting the conditions for ideal MHD in terms of \( \beta \)  and \( \tau_{ii} \), 

1. High collisionality:
$$
\frac{\tau_{ii}}{\tau} = 2.14 \times 10^{12} \frac{T^2}{n L} \ll 1 
$$
$$
\rightarrow T_{eV} \ll 6.8 \times 10^{-7} L_{cm} ^{1/2} n_{cm^{-3}} ^{1/2}
$$
2. Small gyroradius:
$$
\frac{r_{L, i}}{L} = 2.3 \times 10^7 \frac{1}{Z L} \sqrt{ \frac{\mu B}{n}} \ll 1
$$
$$
\rightarrow n_{cm^{-3}} \gg 5.3 \times 10^{14} \frac{\mu B_{T}}{Z^2 L_{cm} ^2}
$$
3. Low resistivity:
$$
\left( \frac{m_e}{m_i} \right) ^{3/2} \left( \frac{r_{L, i}}{L} \right) ^2 \frac{\tau}{\tau_{ii}} = 5.65 \frac{\mu B}{Z^2 L T^2}
$$
$$
\rightarrow T_{eV} \gg 2.4 \frac{\mu ^{3/2} \beta^{1/2}}{Z L _{cm} ^{1.2}}
$$

<p align="center"> <img alt="Figure 12.7" src="../img/12.7.png" /> </p>

## Perpendicular MHD

For most configurations for magnetic fusion confinement, we are able to satisfy 2. and 3. but often have densities much too low to meet the high collisionality constraint. However, in practice ideal MHD does accurately model macroscopic behavior of many plasmas. At the same time, magnetized / fusion plasmas are often largely collisionless. We can understand why by re-writing the collisionality requirement as

$$
1 \gg \frac{\tau_{ii}}{\tau} = \frac{\tau_{ii} v_{T, i}}{\tau v_{T, i}} \sim \frac{\lambda}{L}
$$

where \( \lambda \) is the mean free path. The ratio \( \lambda / L \) is also known as the **Knudsen number**. In magnetized plasmas, the mean free path is often very long, but the path between collisions can cover a great distance only by following magnetic field lines. Motion \( \perp \) to the magnetic field is constrained by \( r_{L, i} \). This suggests an approach wherein we divide the plasma model into a 1-D kinetic model to be solved along the magnetic field and a 2-D MHD model \( \perp \) to the magnetic field. 

We consider diffusivity (terms like viscosity, conductivity) parallel and perpendicular to \( \vec B \) 
$$
k_\parallel \sim \frac{\lambda ^2}{\tau_{ii}}
$$
$$
k_\perp \sim \frac{r_{L, i} ^2}{\tau_{ii}}
$$
$$
\frac{k_\parallel}{k_\perp} \sim \left( \frac{\lambda}{r_{L, i}} \right)^2 \sim (\omega_{c, i} \tau_{ii} )^2
$$

