import sys

def evaluate(numbers, target):
    """
    Recursively evaluates if a combination of operators can make the numbers equal the target.
    """
    if len(numbers) == 1:
        return numbers[0] == target

    for op in ['+', '*', '||']:
        if op == '+':
            result = numbers[0] + numbers[1]
        elif op == '*':
            result = numbers[0] * numbers[1]
        else:  # op == '||'
            result = int(str(numbers[0]) + str(numbers[1]))
        if evaluate([result] + numbers[2:], target):
            return True
    return False

total_calibration = 0

for line in sys.stdin:
    parts = line.strip().split(':')
    target = int(parts[0])
    numbers = [int(x) for x in parts[1].split()]

    if evaluate(numbers, target):
        total_calibration += target

print(total_calibration)