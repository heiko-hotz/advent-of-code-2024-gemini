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

def dfs(grid, r, c, visited, reachable_nines):
  """Performs Depth-First Search to find hiking trails."""
  rows = len(grid)
  cols = len(grid[0])
  
  if grid[r][c] == 9:
      reachable_nines.add((r, c))
      return

  for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    nr, nc = r + dr, c + dc
    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited and grid[nr][nc] == grid[r][c] + 1:
      visited.add((nr, nc))
      dfs(grid, nr, nc, visited, reachable_nines)
      visited.remove((nr, nc))

def calculate_trailhead_score(grid, trailhead):
  """Calculates the score of a trailhead."""
  visited = {trailhead}
  reachable_nines = set()
  dfs(grid, trailhead[0], trailhead[1], visited, reachable_nines)
  return len(reachable_nines)

def main():
  """Reads the map, finds trailheads, calculates scores, and prints the sum."""
  grid = read_map(file=sys.stdin)
  trailheads = find_trailheads(grid)
  total_score = 0
  for trailhead in trailheads:
    total_score += calculate_trailhead_score(grid, trailhead)
  print(total_score)

if __name__ == "__main__":
  import sys
  main()