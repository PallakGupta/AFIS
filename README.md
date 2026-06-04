# AFIS - Anti Fingerprint Instruction Shuffler

## Overview

AFIS is a compiler-inspired code diversification framework developed in Python. The project transforms programs while preserving their behavior by applying optimization and diversification techniques commonly used in compiler backends.

The system parses a custom Intermediate Representation (IR), performs optimization passes, analyzes dependencies and control flow, applies transformations, and verifies semantic equivalence.

---

## Features

### Optimization Passes

* Constant Propagation
* Constant Folding
* Dead Code Elimination

### Program Analysis

* Dependency Graph Construction
* Control Flow Graph (CFG) Construction
* Basic Block Identification

### Diversification Techniques

* Instruction Reordering
* Basic Block Reordering
* Register Renaming

### Verification

* Semantic Equivalence Checking
* Fingerprint Hash Generation
* Diversification Score Calculation

---

## Architecture

Input IR
↓
Parser
↓
Optimizer
↓
CFG Builder
↓
Dependency Analysis
↓
Scheduler
↓
Register Renaming
↓
Verification
↓
Fingerprint Engine

---

## Example

### Input

a = 10
b = 20
c = a + b
print c

### Transformed Output

r764 = 20
r554 = 10
r297 = r554 + r764
print r297

### Result

Semantic Equivalence: PASS

---

## Technologies Used

* Python
* NetworkX
* Git

---

## Future Work

* CFG Visualization
* Advanced Block Scheduling
* Variant Generation Engine
* HTML Reports
* Automated Test Suite
* LLM Assisted Transformation Analysis

---