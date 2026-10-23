# Digital Twin Portfolio

Mechanical & Manufacturing Engineering student building simulation and digital twin projects, from vibration and heat transfer models to a live motor/pump twin.

## Projects

| # | Project | Focus | Status |
|---|---------|-------|--------|
| 1A | Vibration model (1/2-DOF) | Python, ODEs, validation vs analytical | Planned |
| 1B | Heat transfer model | Python + Ansys thermal comparison | Planned |
| 2A | Pump impeller/casing FEA | Fusion 360, Ansys, mesh convergence | Planned |
| 2B | Motor/gearbox housing | Thermal + vibration, design change | Planned |
| 3A | Bench vibration twin | Arduino + calibrated model | Planned |
| 3B | Predictive maintenance | Bearing data, RUL estimate | Planned |
| 4A | Motor/pump digital twin (flagship) | MQTT, Grafana, state estimation | Planned |
| 4B | Production line twin | SimPy discrete-event simulation | Planned |

## Repo structure (one repo per project, same layout)

```
project-name/
├── README.md        # write-up
├── requirements.txt # pinned Python packages
├── docs/            # figures, diagrams, report PDF, demo GIF
├── src/             # code (or CAD/simulation setup notes)
├── data/            # small datasets or links to large ones
└── results/         # plots, tables, exported outputs
```

## Write-up structure for each project

1. **Problem:** the real mechanical/manufacturing question
2. **Approach:** tools and workflow
3. **Model & Assumptions:** equations, geometry, boundary conditions
4. **Validation:** analytical solution, mesh convergence, or measured data
5. **Results:** key plots/tables with interpretation
6. **Limitations:** what the model cannot capture
7. **Next Steps:** what I would do with more time or data

## Contact

LinkedIn:Felix Obuya 
Email:thusfelix@gmail.com 
