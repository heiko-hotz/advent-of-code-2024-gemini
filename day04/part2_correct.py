def solve():
    grid = [list(line.strip()) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])
    target = "MAS"
    count = 0

    def check_mas_seq(positions):
        """
        Checks if the letters at the given positions form "MAS" or "SAM".
        """
        mas_str = ""
        for r, c in positions:
            if 0 <= r < rows and 0 <= c < cols:
                mas_str += grid[r][c]
            else:
                return False  # Out of bounds
        return mas_str == target or mas_str == target[::-1]

    for r in range(1, rows - 1):  # Exclude edges
        for c in range(1, cols - 1):
            # Diagonal from top-left to bottom-right
            diag1 = [(r - 1, c - 1), (r, c), (r + 1, c + 1)]
            # Diagonal from top-right to bottom-left
            diag2 = [(r - 1, c + 1), (r, c), (r + 1, c - 1)]

            if check_mas_seq(diag1) and check_mas_seq(diag2):
                count += 1

    print(count)

import sys
solve()