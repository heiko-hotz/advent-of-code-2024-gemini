def solve():
    grid = []
    while True:
        try:
            line = input()
            grid.append(line)
        except EOFError:
            break

    rows = len(grid)
    cols = len(grid[0])

    antennas = {}
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != '.':
                freq = grid[r][c]
                if freq not in antennas:
                    antennas[freq] = []
                antennas[freq].append((r, c))

    antinodes = set()
    for freq in antennas:
        for i in range(len(antennas[freq])):
            for j in range(i + 1, len(antennas[freq])):
                r1, c1 = antennas[freq][i]
                r2, c2 = antennas[freq][j]

                # Calculate antinode locations
                ar1 = 2 * r1 - r2
                ac1 = 2 * c1 - c2
                ar2 = 2 * r2 - r1
                ac2 = 2 * c2 - c1
                
                ar3 = r1 - (r2-r1)
                ac3 = c1 - (c2-c1)
                ar4 = r2 - (r1-r2)
                ac4 = c2 - (c1-c2)

                # Check bounds and add to set
                if 0 <= ar1 < rows and 0 <= ac1 < cols:
                    antinodes.add((ar1, ac1))
                if 0 <= ar2 < rows and 0 <= ac2 < cols:
                    antinodes.add((ar2, ac2))
                if 0 <= ar3 < rows and 0 <= ac3 < cols:
                    antinodes.add((ar3, ac3))
                if 0 <= ar4 < rows and 0 <= ac4 < cols:
                    antinodes.add((ar4, ac4))

    print(len(antinodes))

solve()