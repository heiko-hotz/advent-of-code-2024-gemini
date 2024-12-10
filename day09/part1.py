def parse_disk_map(disk_map):
    layout = []
    file_id = 0
    i = 0

    while i < len(disk_map):
        file_length = int(disk_map[i])
        if file_length > 0:
            layout.extend([file_id] * file_length)
            file_id += 1
        
        i += 1
        if i < len(disk_map):
            free_space_length = int(disk_map[i])
            layout.extend(["."] * free_space_length)
        
        i += 1

    return layout

def compact_disk(layout):
    while True:
        moved = False
        new_layout = layout[:]
        for i in range(len(layout) - 1):  # Traverse left to right
            if layout[i] == "." and layout[i + 1] != ".":  # Free space followed by a file block
                new_layout[i] = layout[i + 1]
                new_layout[i + 1] = "."
                moved = True
        layout = new_layout
        if not moved:  # If no blocks were moved in this pass, end the process
            break
    return layout

def calculate_checksum(layout):
    checksum = 0
    for pos, block in enumerate(layout):
        if block != ".":
            checksum += pos * block
    return checksum

def main():
    import sys
    # Read input from stdin
    disk_map = sys.stdin.read().strip()

    # Parse the disk map into a layout
    layout = parse_disk_map(disk_map)

    # Compact the disk layout
    compacted_layout = compact_disk(layout)

    # Calculate the checksum
    checksum = calculate_checksum(compacted_layout)

    # Print the result
    print(checksum)

if __name__ == "__main__":
    main()
