# SSD Model Core

## 1. Fundamental Definition

The Sigma–Schmidt Duality (SSD) is defined by the coupling of two components:

- Se(t): extraction component (directed energy / gradient)
- Sa(t): expansion component (geometric / surface-like response)

Core relation:

σ(t) = Se(t) · Sa(t)

---

## 2. Effective Scale Factor

The observable expansion is defined via:

a_eff(t) = σ(t)^(1/3)

This acts as the effective FLRW-like scale factor.

---

## 3. Effective Hubble Parameter

H(t) = (1/3) · (σ̇ / σ)

This replaces the standard definition H = ȧ / a.

---

## 4. Effective Friedmann Structure (Conceptual)

The SSD background model introduces:

H²(t) = (8πG / 3) · ρ_total(t) − k_eff(t) · σ(t)^(-2/3)

with:

ρ_total = ρ_m + ρ_r + ρ_σ + ρ_friction

---

## 5. Separation of Layers

This repository strictly separates:

### A. Core Physics
- σ(t) definition
- Se / Sa structure
- geometric interpretation

### B. Observable Mapping
- a_eff(t)
- H(z)
- distance relations

### C. Fit Layer (Phenomenology)
- empirical modifications
- tanh / ring structures
- parameterized deviations from ΛCDM

---

## 6. Design Principle

SSD must always allow a clean ΛCDM limit.

No test or extension may violate:

lim(SSD → 0) = ΛCDM

---

## 7. Status

This is a working core definition.

Formal derivations and Lagrangian structure are not yet included.

