def is_safe(report):
    levels = list(map(int, report.split()))
    if len(levels) < 2:
        return True
    
    increasing = levels[1] > levels[0]
    
    for i in range(len(levels) - 1):
        diff = levels[i+1] - levels[i]
        if (increasing and diff <= 0) or (not increasing and diff >= 0):
            return False
        if abs(diff) < 1 or abs(diff) > 3:
            return False

    return True

def is_safe_with_dampener(report):
    levels = list(map(int, report.split()))
    if is_safe(report):
        return True
    
    for i in range(len(levels)):
        temp_levels = levels[:i] + levels[i+1:]
        if len(temp_levels) >= 2:
            increasing = temp_levels[1] > temp_levels[0]
            safe = True
            for j in range(len(temp_levels) - 1):
                diff = temp_levels[j+1] - temp_levels[j]
                if (increasing and diff <= 0) or (not increasing and diff >= 0):
                    safe = False
                    break
                if abs(diff) < 1 or abs(diff) > 3:
                    safe = False
                    break
            if safe:
                return True
        elif len(temp_levels) < 2:
            return True
    return False

safe_count = 0
while True:
    try:
        report = input()
        if is_safe_with_dampener(report):
            safe_count += 1
    except EOFError:
        break

print(safe_count)