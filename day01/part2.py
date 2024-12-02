import sys
from collections import Counter

def solve():
    left_list = []
    right_list = []
    
    for line in sys.stdin:
        left, right = map(int, line.strip().split())
        left_list.append(left)
        right_list.append(right)
    
    right_counts = Counter(right_list)
    
    similarity_score = 0
    for num in left_list:
        similarity_score += num * right_counts[num]
    
    print(similarity_score)

solve()