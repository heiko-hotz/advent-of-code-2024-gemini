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

safe_count = 0
while True:
    try:
        report = input()
        if is_safe(report):
            safe_count += 1
    except EOFError:
        break

print(safe_count)