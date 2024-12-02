import sys

def solve():
    left_list = []
    right_list = []
    
    for line in sys.stdin:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)
    
    left_list.sort()
    right_list.sort()
    
    total_distance = 0
    for i in range(len(left_list)):
        total_distance += abs(left_list[i] - right_list[i])
    
    print(total_distance)

solve()