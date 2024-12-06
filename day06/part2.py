def solve():
    grid = []
    start_row, start_col = -1, -1
    with open("day06/input.txt", "r") as f:
        for row_index, line in enumerate(f):
            row = list(line.strip())
            if '^' in row:
                start_row, start_col = row_index, row.index('^')
            grid.append(row)

    rows = len(grid)
    cols = len(grid[0])

    def get_guard_path(grid, start_row, start_col):
        path = []
        visited = set()
        current_row, current_col = start_row, start_col
        direction = 0  # 0: up, 1: right, 2: down, 3: left

        while 0 <= current_row < rows and 0 <= current_col < cols:
            path.append(((current_row, current_col), direction))
            if (current_row, current_col, direction) in visited:
                # Loop detected
                loop_start_index = next(i for i, ((r, c, d)) in enumerate(visited) if (r, c, d) == (current_row, current_col, direction))
                return list(visited)[loop_start_index:], True # Return path and a flag indicating a loop

            visited.add((current_row, current_col, direction))

            next_row, next_col = current_row, current_col
            if direction == 0:
                next_row -= 1
            elif direction == 1:
                next_col += 1
            elif direction == 2:
                next_row += 1
            elif direction == 3:
                next_col -= 1

            if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] != '#':
                current_row, current_col = next_row, next_col
            elif not (0 <= next_row < rows and 0 <= next_col < cols):
                break
            else:
                direction = (direction + 1) % 4

        return path, False  # Return path and False (no loop)

    initial_path, _ = get_guard_path(grid, start_row, start_col) # We don't need the loop flag for the initial path
    initial_path_coords = {pos for pos, _ in initial_path}

    potential_obstacles = set()
    for r, c in initial_path_coords:
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '.' and (nr, nc) != (start_row, start_col):
                potential_obstacles.add((nr, nc))

    loop_count = 0
    for obs_row, obs_col in potential_obstacles:
        new_grid = [row[:] for row in grid]
        new_grid[obs_row][obs_col] = '#'
        new_path, is_loop = get_guard_path(new_grid, start_row, start_col)

        if is_loop:
            loop_count += 1

    print(loop_count)

solve()