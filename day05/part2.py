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

    rules = {}
    for rule in rules_part:
        a, b = rule.split('|')
        rules.setdefault(a, []).append(b)

    total_middle_pages_incorrect = 0
    for update_str in updates_part:
        update = update_str.split(',')
        is_valid = True

        for i in range(len(update)):
            for j in range(len(update)):
                if i == j:
                    continue
                if update[j] in rules.get(update[i], []):
                    try:
                        if update.index(update[i]) > update.index(update[j]):
                            is_valid = False
                            break
                    except ValueError:
                        pass
            if not is_valid:
                break
        
        if not is_valid:
            sorted_update = sort_update(update, rules)
            middle_index = len(sorted_update) // 2
            total_middle_pages_incorrect += int(sorted_update[middle_index])

    print(total_middle_pages_incorrect)

def sort_update(update, rules):
    n = len(update)
    for i in range(n):
        for j in range(0, n - i - 1):
            if violates_rule(update[j+1], update[j], rules):
                update[j], update[j+1] = update[j+1], update[j]
    return update

def violates_rule(page1, page2, rules):
    return page2 in rules.get(page1, [])

solve()