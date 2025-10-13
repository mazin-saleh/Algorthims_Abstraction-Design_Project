<!--
Project-specific Copilot instructions for contributors and automated coding agents.
Keep this file short, concrete, and tied to discoverable code patterns.
-->
# Copilot / AI instructions (project-specific)

This is a small algorithms project with two solution entry points: `src/program1.py` and `src/program2.py`.
Follow these concrete rules when making edits, writing solutions, or generating code:

- Big picture
  - Each `program*.py` implements a single function (respectively `program1` and `program2`) that must keep the declared
    signature and return types: e.g. `def program1(n: int, k: int, values: List[int]) -> Tuple[int, List[int]]`.
  - The repository contains problem statements / assignment PDFs in `docs/` (for example `COP4533fa25ProgrammingProjectGreedy&DP (1).pdf`).
    Use those PDFs to infer intended problem constraints before changing algorithmic behavior.

- I/O contract and examples (do not change)
  - Each `program*.py` has a `__main__` block that reads from stdin:
    - First line: `n k` (integers)
    - Second line: space-separated `values` (n integers)
    - Output: first print the maximal total value, then print each chosen index on its own line.
  - Indices are 1-indexed in the expected output (see the existing `print` loop in each file).
  - Do not modify the `__main__` parsing or the function name/signature; tests (or graders) call the script exactly this way.

- Implementation notes and patterns to follow
  - Keep type annotations and return a Tuple[int, List[int]]: (max_value, chosen_indices).
  - Replace only the placeholder return and the "Add you code here" area. Avoid changing imports or top-level structure.
  - Solutions should be correct for edge cases implied by PDFs: small n (including n=0 or n=1), k >= n, and negative/zero values.

- Project conventions
  - Minimal, single-file solution per problem. No external dependencies or test harnesses are present in the repo.
  - Use plain Python 3 (the environment uses the system Python). Keep solutions short and readable.

- How to run locally (example)
  - Run a solution interactively (zsh / bash):
    ```bash
    python3 src/program1.py
    # then paste input like:
    # 5 1
    # 2 7 9 3 1
    ```

- Where to look for more context
  - `docs/` — assignment/problem PDFs (source of constraints and grading rules).
  - `src/program1.py` and `src/program2.py` — canonical input/output format and the placeholder implementation locations.

If anything in these instructions seems incomplete or you need additional examples (unit tests, stronger I/O validation, or a runner), ask and I will extend this file.
