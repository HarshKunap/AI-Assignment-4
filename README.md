# Constraint Satisfaction Systems

A collection of artificial intelligence implementations focused on solving real-world and classical problems using Constraint Satisfaction Problem (CSP) techniques and recursive backtracking.

## Overview

This repository explores how complex problems can be modeled using variables, domains, and constraints, and solved systematically through search and constraint validation.

The project includes multiple CSP-based implementations ranging from map coloring and puzzle solving to symbolic arithmetic reasoning.

## Implemented Systems

### Map Coloring for Australia

A graph coloring implementation where regions of Australia are assigned colors such that neighboring states do not share the same color.

Concepts explored:

- Constraint propagation
- Graph-based representations
- Backtracking search
- State validation

### Telangana District Map Coloring

A larger-scale map coloring problem involving district-level adjacency constraints.

The implementation includes graph visualization using NetworkX and Matplotlib to represent geographic relationships and final solutions.

Concepts explored:

- Large-scale CSP modeling
- Graph visualization
- Adjacency constraints
- Search optimization

### Sudoku Solver and Generator

A complete Sudoku-solving system capable of generating and solving playable 9x9 Sudoku puzzles using recursive search and constraint validation.

Concepts explored:

- Recursive backtracking
- Constraint checking
- Grid optimization
- Search-space pruning

### Cryptarithmetic Solver

A generalized symbolic arithmetic solver that assigns valid digit mappings to letters in word-based arithmetic equations.

Default implementation solves:

```text
CROSS + ROADS = DANGER
```

Concepts explored:

- Symbolic reasoning
- Constraint enforcement
- Combinatorial search
- Logical validation

## Core Concepts

This project explores foundational concepts in artificial intelligence, including:

- Constraint Satisfaction Problems (CSP)
- Backtracking algorithms
- Recursive search strategies
- Constraint validation
- Graph-based problem modeling
- Combinatorial optimization

## Tech Stack

- Python
- NetworkX
- Matplotlib
- Graph Theory Concepts
- Artificial Intelligence Fundamentals

## Project Structure

```text
australia_map_coloring.py
telangana_map_coloring.py
sudoku_solver.py
cryptarithmetic_solver.py
```

## Getting Started

Run individual modules using:

```bash
python australia_map_coloring.py
python sudoku_solver.py
python cryptarithmetic_solver.py
python telangana_map_coloring.py
```

Optional dependencies for graph visualization:

```bash
pip install networkx matplotlib
```

## Key Takeaways

Through this project, I explored:

- Modeling problems using constraints
- Efficient search strategies in AI systems
- Recursive reasoning techniques
- Graph-based problem solving
- Performance tradeoffs in combinatorial search

---

This repository reflects an exploration of intelligent problem-solving systems and foundational approaches in artificial intelligence.