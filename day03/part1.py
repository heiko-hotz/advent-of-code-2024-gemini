import re
import sys

def solve():
    total_sum = 0
    for line in sys.stdin:
        matches = re.findall(r'mul\((\d{1,3}),(\d{1,3})\)', line)
        for match in matches:
            num1, num2 = map(int, match)
            total_sum += num1 * num2
    print(total_sum)

solve()