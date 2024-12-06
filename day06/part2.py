def solve():
    grid = [list(line.strip()) for line in sys.stdin]
    rows, cols = len(grid), len(grid[0])
    print(f"Grid size: {rows}x{cols}")

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

    print(f"Starting position: ({start_r}, {start_c}) facing {start_dir}")

    directions = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}
    right_turns = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    def get_path(grid, start_r, start_c, start_dir):
        path = []
        r, c = start_r, start_c
        curr_dir = start_dir
        max_path_length = rows * cols  # No path should be longer than the grid size
        
        while 0 <= r < rows and 0 <= c < cols and len(path) < max_path_length:
            path.append((r, c))
            dr, dc = directions[curr_dir]
            next_r, next_c = r + dr, c + dc
            if 0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#':
                curr_dir = right_turns[curr_dir]
                dr, dc = directions[curr_dir]
                next_r, next_c = r + dr, c + dc
                if not (0 <= next_r < rows and 0 <= next_c < cols) or (0 <= next_r < rows and 0 <= next_c < cols and grid[next_r][next_c] == '#'):
                    break
            r, c = next_r, next_c
        
        return path if len(path) < max_path_length else None
    
    count = 0
    total_cells = rows * cols
    cells_checked = 0
    
    for r in range(rows):
        for c in range(cols):
            cells_checked += 1
            if cells_checked % 100 == 0:  # Update every 100 cells
                print(f"Progress: {cells_checked}/{total_cells} cells checked ({(cells_checked/total_cells)*100:.1f}%)")
            
            if (r,c) == (start_r, start_c) or grid[r][c] == '#':
                continue
                
            temp_grid = [row[:] for row in grid]
            temp_grid[r][c] = '#'
            new_path = get_path(temp_grid, start_r, start_c, start_dir)
            
            if new_path and (new_path[-1][0], new_path[-1][1]) in new_path[:-1]:
                count += 1
                print(f"Found valid loop at ({r}, {c}). Current count: {count}")

    print(f"\nFinal result: {count}")

import sys
solve()