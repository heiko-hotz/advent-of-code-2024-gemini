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
        if len(antennas[freq]) < 2:
            continue
            
        for r in range(rows):
          for c in range(cols):
            count = 0
            for i in range(len(antennas[freq])):
              for j in range(i+1, len(antennas[freq])):
                r1, c1 = antennas[freq][i]
                r2, c2 = antennas[freq][j]
                if (r2-r1)*(c-c1) == (r-r1)*(c2-c1):
                  count+=1
                  break
              if count > 0:
                break
            if count > 0:
              antinodes.add((r,c))
    
        for r, c in antennas[freq]:
            antinodes.add((r, c))
    print(len(antinodes))

solve()