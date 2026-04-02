AI Assignment: Constraint Satisfaction Problems (CSP)
Overview
This project contains Python implementations of four problems modeled as Constraint Satisfaction Problems (CSPs). Each problem is solved using a recursive backtracking search algorithm combined with strict constraint checking.

1. Map Coloring (Australia)
Problem
Assign colors to the seven principal states and territories of Australia so that no two adjacent regions share the same color.

Approach
Variables: States (WA, NT, Q, SA, NSW, V, T)

Domain: {Red, Green, Blue}

Constraints: Neighboring states must have completely different colors

Method: Backtracking Search

2. Telangana Map Coloring
Problem
Assign colors to the 33 districts of Telangana so that adjacent districts do not share the same color.

Approach
Variables: 33 Districts (e.g., Hyderabad, Rangareddy)

Domain: {Red, Green, Blue}

Constraints: Adjacent districts must have different colors

Method: Backtracking Search

Visualization
Built using NetworkX and Matplotlib libraries

Districts are represented as graph nodes

Adjacency is represented with connecting edges

The final color assignment is displayed in a visual graph

3. Sudoku Solver & Generator
Problem
Programmatically solve a 9x9 Sudoku board and generate a playable puzzle by removing a specific number of cells.

CSP Formulation
Variables: Every cell in the 9x9 grid

Domain: Integers {1 - 9}

Constraints:

No repeated values in any horizontal row

No repeated values in any vertical column

No repeated values in any 3x3 subgrid block

Method: Randomized backtracking search over empty cells with constant constraint checks

4. Universal Cryptarithmetic Solver
Problem
Assign unique digits to letters to solve word addition puzzles (configured by default to solve CROSS + ROADS = DANGER).

CSP Formulation
Variables: Dynamically extracted unique letters from the provided words

Domain: Digits {0 - 9}

Constraints:

All unique letters must map to unique digits

No leading zeros allowed for the first letter of any word

The mathematical equation must hold exactly

Method: Backtracking assignment of digits to letters with validation on final complete assignments

Concepts Used
Constraint Satisfaction Problems (CSP)

Backtracking Algorithm

Constraint Checking & Validation

Recursion

Graph Representation

Project Files
australia_map_coloring.py

telangana_map_coloring.py

sudoku_solver.py

cryptarithmetic_solver.py

How to Run
Run each script directly through Python in your terminal:

Bash
python australia_map_coloring.py
python sudoku_solver.py
python cryptarithmetic_solver.py
python telangana_map_coloring.py
Optional Dependencies
(Required only for the Telangana visualization graph)

Bash
pip install networkx matplotlib
Conclusion
These implementations demonstrate how map coloring, Sudoku generation, and cryptarithmetic logic can be modeled and solved as CSPs using the backtracking algorithm.