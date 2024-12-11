def transform_stones(stones):
    """Transforms a list of stones according to the given rules."""
    new_stones = []
    for stone in stones:
        s_stone = str(stone)
        if stone == 0:
            new_stones.append(1)
        elif len(s_stone) % 2 == 0:
            mid = len(s_stone) // 2
            new_stones.append(int(s_stone[:mid]))
            new_stones.append(int(s_stone[mid:]))
        else:
            new_stones.append(stone * 2024)
    return new_stones

# Read initial stones from input
initial_stones = list(map(int, input().split()))

# Perform 25 blinks
stones = initial_stones
for _ in range(25):
    stones = transform_stones(stones)

# Print the final number of stones
print(len(stones))