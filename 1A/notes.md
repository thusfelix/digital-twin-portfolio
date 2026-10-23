Free Vibration of a Spring-Mass-Damper

1. The model
A mass m on a spring (stiffness k) with a damper (coefficient c).
Forces: spring = -k·x, damper = -c·(dx/dt), inertia = m·(d²x/dt²).

Equation of motion:

m·x'' + c·x' + k·x = 0

2. Key quantities
- Natural angular frequency: ωn = sqrt(k/m) [rad/s]; in Hz: fn = ωn / (2π)
- Critical damping: c_crit = 2·sqrt(k·m) [N·s/m]
- Damping ratio: ζ = c / c_crit (dimensionless)
-
- 3. Behaviour by damping ratio
- ζ < 1 (under-damped): oscillates, amplitude decays gradually
- ζ = 1 (critically damped): fastest return to rest, no oscillation
- ζ > 1 (over-damped): slow return to rest, no oscillation

4. Worked example
Motor: m = 20 kg, k = 50,000 N/m, c = 200 N·s/m

- ωn = sqrt(50000 / 20) = 50 rad/s (about 7.96 Hz)
- c_crit = 2·sqrt(50000 × 20) = 2000 N·s/m
- ζ = 200 / 2000 = 0.1 (lightly damped, rings for a while)

5. Questions

Q1. If I double the mass, does ωn go up or down, and by what factor?
My answer: decreases natural angular frequency by factor sqrt2

Q2. Why are motor mounts usually under-damped rather than critically damped?
My answer: provides sufficient vibration isolation at a lower cost

Q3. What does ζ = 0 mean physically?
My answer: no energy is dissipated during dumping
