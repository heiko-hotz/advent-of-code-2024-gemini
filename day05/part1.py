def solve():
    rules_part, updates_part = [], []
    mode = "rules"

    while True:
        try:
            line = input()
            if not line:
                mode = "updates"
                continue
            if mode == "rules":
                rules_part.append(line)
            else:
                updates_part.append(line)
        except EOFError:
            break

    # Parse rules into a dictionary where keys are 'before' pages
    # and values are lists of 'after' pages
    rules = {}
    for rule in rules_part:
        a, b = rule.split('|')
        rules.setdefault(a, []).append(b)

    total_middle_pages = 0
    for update_str in updates_part:
        update = update_str.split(',')
        is_valid = True

        # Check all pairs of pages in the update
        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                # If rule exists for update[i] | update[j]
                if update[j] in rules.get(update[i], []):
                    # Check if update[i] comes before update[j]
                    try:
                        if update.index(update[i]) > update.index(update[j]):
                            is_valid = False
                            break
                    except ValueError:
                        # One of the pages not in the update
                        pass
            if not is_valid:
                break

        if is_valid:
            middle_index = len(update) // 2
            total_middle_pages += int(update[middle_index])

    print(total_middle_pages)

solve()