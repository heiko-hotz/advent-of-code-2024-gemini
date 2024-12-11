def transform_stone(stone):
    """Transforms a single stone value according to the given rules."""
    s_stone = str(stone)
    if stone == 0:
        return [1]
    elif len(s_stone) % 2 == 0:
        mid = len(s_stone) // 2
        return [int(s_stone[:mid]), int(s_stone[mid:])]
    else:
        return [stone * 2024]

# Read initial stones from input
initial_stones = list(map(int, input().split()))

# Initialize stone counts
stone_counts = {}
for stone in initial_stones:
    stone_counts[stone] = stone_counts.get(stone, 0) + 1

# Perform 75 blinks
for _ in range(75):
    new_stone_counts = {}
    for stone, count in stone_counts.items():
        transformed_stones = transform_stone(stone)
        for new_stone in transformed_stones:
            new_stone_counts[new_stone] = new_stone_counts.get(new_stone, 0) + count
    stone_counts = new_stone_counts

# Calculate the total number of stones
total_stones = sum(stone_counts.values())

# Print the final number of stones
print(total_stones)