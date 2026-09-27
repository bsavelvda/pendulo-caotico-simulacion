# Chaotic Pendulum Simulation & Poincaré Section

Computational physics simulation in Python analyzing a driven, damped pendulum in the chaotic regime using the Euler-Cromer integration method.

## Project Overview

The nonlinear dynamics of the system are governed by the differential equation:

$$\frac{d^2\theta}{dt^2} = -\frac{g}{L}\sin(\theta) - \gamma \omega + A \cos(\omega_d t)$$

Where:
* $\theta$: Angular displacement
* $\omega$: Angular velocity
* $\gamma$: Damping coefficient
* $A$: Driving force amplitude
* $\omega_d$: Driving frequency

The simulation examines time evolution, phase space trajectories, and a **Poincaré Section** to visualize the fractal geometry of the underlying strange attractor.

## Visualizations

![Poincaré Section](outputs/poincare_pendulo.svg)

## Execution

To run the simulation locally:

```bash
python3 src/pendulo.py
