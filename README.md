# Meep simulations starter

This workspace is a minimal starting point for learning finite-difference time-domain (FDTD) simulations with Meep.

## 1. Create a virtual environment

```bash
cd /home/biji/meep_projects
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install Meep

If your environment supports it, use:

```bash
python -m pip install --upgrade pip
python -m pip install meep
```

If that fails on your system, try the conda-forge route instead:

```bash
conda install -c conda-forge pymeep
```

## 3. Run the sample simulation

```bash
python sim_basic.py
```

The script sets up a tiny 2D simulation with a dielectric block and a Gaussian source. It is intentionally simple so you can edit it to explore different geometries, sources, and boundary conditions.

## 4. Learn by changing one thing at a time

- Change the source frequency
- Move the source location
- Change the dielectric block size or material
- Add more blocks or a waveguide
- Try different boundary layers and simulation lengths

## 5. Useful next steps

- Read the Meep documentation examples
- Start with 1D and 2D cases before moving to 3D
- Save field data and inspect it after the run
- Plot the output with Python libraries such as matplotlib
