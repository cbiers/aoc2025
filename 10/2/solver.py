#!/usr/bin/env python3
"""
Integer-only version.

For each line encoding a system, solve:
    minimize sum(bi)
    subject to A b = rhs, bi >= 0, bi integer
Then sum the per-line minima across the file.

Requires:
    pip install ortools
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from typing import List, Tuple

import numpy as np

try:
    from ortools.sat.python import cp_model
except ImportError:
    cp_model = None


@dataclass
class Parsed:
    tuples: List[Tuple[int, ...]]  # variable -> equation indices
    rhs: np.ndarray                # shape (m,)


LINE_RE = re.compile(r"""
    ^\s*
    (?:\[[^\]]*\]\s*)?                 # optional bracket part (ignored)
    (?P<tuples>(?:\([^\)]*\)\s*)+)     # one or more (...) groups
    \{(?P<rhs>[^\}]*)\}                # {...}
    \s*$
""", re.VERBOSE)


def parse_line(line: str) -> Parsed:
    m = LINE_RE.match(line)
    if not m:
        raise ValueError(f"Could not parse line: {line.strip()}")

    tuples_blob = m.group("tuples")
    rhs_blob = m.group("rhs")

    tup_strs = re.findall(r"\([^\)]*\)", tuples_blob)
    tuples: List[Tuple[int, ...]] = []
    for ts in tup_strs:
        inside = ts.strip()[1:-1].strip()
        if inside == "":
            tuples.append(tuple())
        else:
            tuples.append(tuple(int(x.strip()) for x in inside.split(",") if x.strip() != ""))

    rhs_vals = [float(x.strip()) for x in rhs_blob.split(",") if x.strip() != ""]
    rhs = np.array(rhs_vals, dtype=float)

    return Parsed(tuples=tuples, rhs=rhs)


def build_matrix(parsed: Parsed) -> Tuple[np.ndarray, np.ndarray]:
    b = parsed.rhs
    m = b.shape[0]
    n = len(parsed.tuples)
    A = np.zeros((m, n), dtype=int)
    for i, eq_idxs in enumerate(parsed.tuples):
        for k in eq_idxs:
            if k < 0 or k >= m:
                raise ValueError(f"Variable b{i} refers to equation {k}, but RHS has only {m} equations.")
            A[k, i] = 1
    return A, b


def solve_ilp_min_sum(A: np.ndarray, rhs: np.ndarray):
    """
    Solve min sum(bi) s.t. A b = rhs, b integer >=0.
    Returns (success: bool, obj: int|None, sol: list[int]|None, message: str)
    """
    if cp_model is None:
        return (False, None, None, "ortools not installed")

    # CP-SAT requires integer RHS
    if np.any(np.abs(rhs - np.round(rhs)) > 1e-9):
        return (False, None, None, "RHS contains non-integers; integer solution impossible under exact equality.")
    bvec = np.round(rhs).astype(int)

    m, n = A.shape

    # Quick impossibility checks for nonnegativity:
    if np.any(bvec < 0):
        return (False, None, None, "Negative RHS with nonnegative vars is infeasible.")

    model = cp_model.CpModel()

    # Safe upper bound: in any equation sum of some vars = RHS -> each var <= max(rhs)
    ub = int(np.max(bvec)) if bvec.size else 0
    # If ub is 0, variables are forced to 0
    vars_b = [model.NewIntVar(0, ub, f"b{i}") for i in range(n)]

    # Add equations A b = rhs
    for k in range(m):
        idxs = [i for i in range(n) if A[k, i] != 0]
        # sum of selected variables equals RHS
        model.Add(sum(vars_b[i] for i in idxs) == int(bvec[k]))

    # Objective: minimize sum(bi)
    model.Minimize(sum(vars_b))

    solver = cp_model.CpSolver()
    solver.parameters.max_time_in_seconds = 10.0  # adjust if needed
    solver.parameters.num_search_workers = 8

    status = solver.Solve(model)

    if status in (cp_model.OPTIMAL, cp_model.FEASIBLE):
        sol = [int(solver.Value(v)) for v in vars_b]
        obj = int(sum(sol))
        return (True, obj, sol, "ok")
    elif status == cp_model.INFEASIBLE:
        return (False, None, None, "infeasible")
    else:
        return (False, None, None, f"solver status {status}")


def main() -> int:
    if len(sys.argv) < 2:
        print("Usage: python solve_sum_int.py <input_file> [--quiet]")
        return 2

    if cp_model is None:
        print("ERROR: ortools not installed. Install with:\n  pip install ortools")
        return 2

    path = sys.argv[1]
    quiet = "--quiet" in sys.argv[2:]

    total = 0
    feasible = 0
    infeasible = 0

    with open(path, "r", encoding="utf-8") as f:
        lines = [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]

    for idx, line in enumerate(lines, start=1):
        try:
            parsed = parse_line(line)
            A, rhs = build_matrix(parsed)
            ok, obj, sol, msg = solve_ilp_min_sum(A, rhs)
        except Exception as e:
            infeasible += 1
            if not quiet:
                print(f"Line {idx}: ERROR: {e}\n  {line}")
            continue

        if ok:
            feasible += 1
            total += int(obj)
            if not quiet:
                print(f"Line {idx}: min integer sum = {obj}  solution={sol}")
        else:
            infeasible += 1
            if not quiet:
                print(f"Line {idx}: FAIL ({msg})")

    print("\n=== TOTALS ===")
    print(f"Feasible lines:   {feasible}")
    print(f"Infeasible lines: {infeasible}")
    print(f"Sum of minima:    {total}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
