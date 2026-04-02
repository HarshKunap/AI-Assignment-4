# ============================================================
#  Map Coloring Problem — CSP (Constraint Satisfaction)
#  Seven principal states/territories of Australia:
#  WA, NT, Queensland (Q), SA, NSW, Victoria (V), Tasmania (T)
# ============================================================

# ── 1. Problem Definition ────────────────────────────────────

VARIABLES = ['WA', 'NT', 'Q', 'SA', 'NSW', 'V', 'T']

DOMAINS = {var: ['Red', 'Green', 'Blue'] for var in VARIABLES}

# Undirected adjacency (no two neighbours share the same colour)
CONSTRAINTS = [
    ('WA',  'NT'),
    ('WA',  'SA'),
    ('NT',  'SA'),
    ('NT',  'Q'),
    ('SA',  'Q'),
    ('SA',  'NSW'),
    ('SA',  'V'),
    ('Q',   'NSW'),
    ('NSW', 'V'),
    # Tasmania (T) is an island — no land borders
]

# ── 2. Constraint Check ──────────────────────────────────────

def is_consistent(variable, color, assignment):
    """Return True if assigning *color* to *variable* violates no constraint."""
    for (x, y) in CONSTRAINTS:
        if x == variable and y in assignment and assignment[y] == color:
            return False
        if y == variable and x in assignment and assignment[x] == color:
            return False
    return True

# ── 3. Backtracking Search ───────────────────────────────────

def backtrack(assignment, domains):
    """Recursive backtracking — returns a complete assignment or None."""

    # Goal test: all variables assigned
    if len(assignment) == len(VARIABLES):
        return assignment

    # Select next unassigned variable (simple left-to-right order)
    unassigned = [v for v in VARIABLES if v not in assignment]
    var = unassigned[0]

    for color in domains[var]:
        if is_consistent(var, color, assignment):
            assignment[var] = color
            result = backtrack(assignment, domains)
            if result is not None:
                return result
            del assignment[var]           # backtrack

    return None   # trigger backtrack in caller

# ── 4. Solve & Display ───────────────────────────────────────

def solve():
    print("=" * 50)
    print("  Map Coloring CSP — Australia")
    print("=" * 50)
    print(f"\nVariables : {VARIABLES}")
    print(f"Colors    : {DOMAINS['WA']}")
    print(f"Constraints ({len(CONSTRAINTS)} pairs):")
    for pair in CONSTRAINTS:
        print(f"  {pair[0]} ≠ {pair[1]}")

    solution = backtrack({}, DOMAINS)

    print("\n" + "-" * 50)
    if solution:
        print("  ✅  Solution found!\n")
        for state in VARIABLES:
            print(f"  {state:<12} →  {solution[state]}")

        # Verify all constraints
        violations = [
            f"{x}-{y}" for (x, y) in CONSTRAINTS
            if solution.get(x) == solution.get(y)
        ]
        print("\n  Constraint check:", "All satisfied ✓" if not violations
              else f"Violations: {violations}")
    else:
        print("  ❌  No solution exists.")
    print("=" * 50)

# ── 5. Entry Point ───────────────────────────────────────────

if __name__ == "__main__":
    solve()