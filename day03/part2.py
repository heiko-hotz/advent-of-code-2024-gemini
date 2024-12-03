import re
import sys

def solve():
    total_sum = 0
    mul_enabled = True
    for line in sys.stdin:
        matches = re.findall(r'(do\(\))|(don\'t\(\))|(mul\((\d{1,3}),(\d{1,3})\))', line)
        for match in matches:
            if match[0] == 'do()':
                mul_enabled = True
            elif match[1] == 'don\'t()':
                mul_enabled = False
            elif match[2] and mul_enabled:
                num1, num2 = map(int, (match[3], match[4]))
                total_sum += num1 * num2
    print(total_sum)

solve()