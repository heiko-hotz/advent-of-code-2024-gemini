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
    visited = set()
    current_row, current_col = start_row, start_col
    direction = 0  # 0: up, 1: right, 2: down, 3: left

    while 0 <= current_row < rows and 0 <= current_col < cols:
        visited.add((current_row, current_col))

        next_row, next_col = current_row, current_col
        if direction == 0:
            next_row -= 1
        elif direction == 1:
            next_col += 1
        elif direction == 2:
            next_row += 1
        elif direction == 3:
            next_col -= 1

        # Check if the next position is within bounds and not an obstacle
        if 0 <= next_row < rows and 0 <= next_col < cols and grid[next_row][next_col] != '#':
            current_row, current_col = next_row, next_col
        elif not (0 <= next_row < rows and 0 <= next_col < cols):
            # Exit the loop if the next position is out of bounds
            break;
        else:
            direction = (direction + 1) % 4

    print(len(visited))

solve()