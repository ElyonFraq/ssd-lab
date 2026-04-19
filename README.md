# ssd-lab

Reproducible microtest lab for the Sigma–Schmidt Duality (SSD).

## Purpose

This repository is being built as a clean, reproducible research workspace for the Sigma–Schmidt Duality.

Its purpose is to:

- document the SSD core model
- separate core physics from observational mapping and phenomenological fits
- develop small reproducible Python test pipelines
- prepare controlled comparisons against standard cosmological baselines
- organize stable work, experimental work, and archived material in a strict way

This repository is not a finished theory package.
It is a structured research lab.

---

## Current Core Working Basis

The current SSD working core is:

σ(t) = Se(t) · Sa(t)

a_eff(t) = σ(t)^(1/3)

H(t) = (1/3) · (σ̇ / σ)

with an effective background idea based on:

- ρ_m
- ρ_r
- ρ_σ
- ρ_friction
- k_eff

These definitions are treated here as the current working basis, not as a finalized derivation.

---

## Scientific Separation Principle

This repository enforces a strict separation between:

### 1. Core Physics
Examples:
- definition of σ(t)
- role of Se and Sa
- effective expansion structure

### 2. Observable Mapping
Examples:
- a_eff(t)
- H(z)
- distance relations
- lookback time

### 3. Fit / Phenomenology Layer
Examples:
- empirical tanh forms
- ring-like modulation ideas
- helper fit functions

Phenomenology must never be presented as core physics.

---## Current Documentation

- `docs/model_core.md` — current SSD core working definition
- `docs/roadmap.md` — phased build plan for the repository

## Repository Structure

```text
ssd-lab/
├── docs/        # model definitions, roadmap, notes
├── scripts/     # reproducible Python scripts
├── tests/       # validation and sanity tests
├── data/        # local data placeholders / loaders / metadata
├── results/     # saved figures, tables, outputs
├── notebooks/   # exploratory work only
└── archive/     # old, unstable, or deprecated material
