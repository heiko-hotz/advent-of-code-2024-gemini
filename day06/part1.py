def solve():
    grid = [list(line.strip()) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])

    # Find starting position and direction
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] in ['^', '>', 'v', '<']:
                start_r, start_c = r, c
                start_dir = grid[r][c]
                grid[r][c] = '.'
                break
        else:
            continue
        break

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    visited = set()
    r, c = start_r, start_c
    curr_dir = start_dir

    while 0 <= r < rows and 0 <= c < cols:
        visited.add((r, c))

        dr, dc = directions[curr_dir]
        next_r, next_c = r + dr, c + dc

        # Only turn if the next position is within bounds and is an obstacle
        if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#':
            curr_dir = right_turns[curr_dir]
            dr, dc = directions[curr_dir]
            next_r, next_c = r + dr, c + dc
            # Check again after turning, if still blocked or out of bounds, then stop
            if not (0 <= next_r < rows and 0 <= next_c < cols) or (0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#'):
                break
        
        r, c = next_r, next_c

    print(len(visited))

import sys
solve()