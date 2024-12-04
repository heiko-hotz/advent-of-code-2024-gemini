def solve():
    grid = [list(line.strip()) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    count = 0

    directions = [
        (0, 1),  # Right
        (1, 0),  # Down
        (1, 1),  # Down-Right
        (1, -1), # Down-Left
        (0, -1), # Left
        (-1, 0), # Up
        (-1, -1),# Up-Left
        (-1, 1)  # Up-Right
    ]

    for r in range(rows):
        for c in range(cols):
            for dr, dc in directions:
                found = True
                for i in range(len(target)):
                    nr, nc = r + i * dr, c + i * dc
                    if not (0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == target[i]):
                        found = False
                        break
                if found:
                    count += 1

    print(count)

import sys
solve()