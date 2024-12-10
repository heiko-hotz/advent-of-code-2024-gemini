def read_map(file):
    """Reads the topographic map from the input file."""
    grid = []
    for line in file:
        grid.append([int(x) for x in line.strip()])
    return grid

def find_trailheads(grid):
    """Finds all trailheads (positions with height 0)."""
    trailheads = []
    for r, row in enumerate(grid):
        for c, height in enumerate(row):
            if height == 0:
                trailheads.append((r, c))
    return trailheads

def dfs(grid, r, c, visited, trail_count):
    """Performs Depth-First Search to count distinct hiking trails."""
    rows = len(grid)
    cols = len(grid[0])

    if grid[r][c] == 9:
        trail_count[(r, c)] = trail_count.get((r, c), 0) + 1
        return

    for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nr, nc = r + dr, c + dc
        if (
            0 <= nr < rows
            and 0 <= nc < cols
            and grid[nr][nc] == grid[r][c] + 1
        ):
            visited.add((nr, nc))
            dfs(grid, nr, nc, visited, trail_count)

def calculate_trailhead_rating(grid, trailhead):
    """Calculates the rating of a trailhead (number of distinct trails)."""
    visited = {trailhead}
    trail_count = {}
    dfs(grid, trailhead[0], trailhead[1], visited, trail_count)
    return sum(trail_count.values())

def main():
    """Reads the map, finds trailheads, calculates ratings, and prints the sum."""
    grid = read_map(file=sys.stdin)
    trailheads = find_trailheads(grid)
    total_rating = 0
    for trailhead in trailheads:
        total_rating += calculate_trailhead_rating(grid, trailhead)
    print(total_rating)

if __name__ == "__main__":
    import sys
    main()