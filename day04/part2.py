def solve():
    grid = [list(line.strip()) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])
    target = "MAS"
    count = 0

    def check_mas(r, c, dr, dc):
        """
        Checks if a "MAS" sequence is valid in the given direction.

        Args:
          r: Starting row.
          c: Starting column.
          dr: Row direction (delta).
          dc: Column direction (delta).

        Returns:
          True if a valid "MAS" (or "SAM") is found, False otherwise.
        """
        mas_str = ""
        for i in range(3):
            nr, nc = r + i * dr, c + i * dc
            if 0 <= nr < rows and 0 <= nc < cols:  # Strict bounds checking
                mas_str += grid[nr][nc]
            else:
                return False  # Out of bounds
        return mas_str == target or mas_str == target[::-1]

    for r in range(1, rows - 1):  # Iterate through potential center rows (excluding edges)
        for c in range(1, cols - 1):  # Iterate through potential center columns (excluding edges)

            # Check all possible X shapes with explicit bounds checks in check_mas function
            if check_mas(r - 1, c - 1, 1, 1) and check_mas(r + 1, c - 1, -1, 1):
                count += 1
            if check_mas(r - 1, c + 1, 1, -1) and check_mas(r + 1, c + 1, -1, -1):
                count += 1
            if check_mas(r - 1, c - 1, 0, 1) and check_mas(r + 1, c - 1, 0, 1):
                count += 1
            if check_mas(r - 1, c - 1, 1, 0) and check_mas(r - 1, c + 1, 1, 0):
                count += 1
            if check_mas(r - 1, c + 1, 0, -1) and check_mas(r + 1, c + 1, 0, -1):
                count += 1
            if check_mas(r + 1, c - 1, -1, 0) and check_mas(r + 1, c + 1, -1, 0):
                count += 1

    print(count)

import sys
solve()