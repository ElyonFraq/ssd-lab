# SSD Roadmap

## Phase 1 — Core Definition
Goal: define the minimal scientific backbone of the repository.

Includes:
- SSD core equations
- separation between core physics, observable mapping, and fit layer
- repository principles
- clean ΛCDM limit requirement

Main file:
- docs/model_core.md

---

## Phase 2 — Repository Structure
Goal: make the repository clean, navigable, and reproducible.

Includes:
- README
- docs/
- scripts/
- tests/
- data/
- results/
- archive/
- notebooks/

Deliverables:
- professional folder structure
- .gitignore
- requirements.txt

---

## Phase 3 — Minimal SSD Python Core
Goal: create a small reproducible code base for the SSD background logic.

Includes:
- sigma definitions
- a_eff computation
- H(t) / H(z) helper functions
- parameter container
- plotting utilities

Target:
- scripts/ contains runnable minimal SSD modules
- tests/ contains basic validation tests

---

## Phase 4 — Observation Pipeline
Goal: connect SSD background logic to observable cosmology.

Includes:
- redshift mapping
- distance integrals
- lookback time
- comparison against ΛCDM baseline

Priority targets:
- lookback
- H(z)
- simple distance functions

---

## Phase 5 — Data-Ready Infrastructure
Goal: prepare the repo for real observational tests.

Includes:
- data folder rules
- loader scripts
- standard result output structure
- reproducible file naming
- metadata notes

Target datasets:
- BAO
- Pantheon
- later: additional probes if needed

---

## Phase 6 — First Real Microtests
Goal: run small controlled SSD vs ΛCDM checks.

Examples:
- sanity-limit tests
- lookback comparison
- H(z) comparison
- simple BAO background checks

Principle:
no large claim before stable small tests

---

## Phase 7 — Extended Phenomenology
Goal: test optional SSD phenomenological extensions only after the core is stable.

Includes:
- tanh structures
- ring-like late-time features
- empirical helper fits

Important:
Phenomenology must never be confused with core physics.

---

## Phase 8 — Paper-Ready Outputs
Goal: make the repo usable for transparent scientific writing.

Includes:
- exportable figures
- saved tables
- run logs
- versioned outputs
- reproducible result folders

---

## Repository Rule

This repository is organized in three layers:

1. Core
2. Workshop
3. Archive

Only stabilized components move from workshop to core.
Old or abandoned material goes to archive.
