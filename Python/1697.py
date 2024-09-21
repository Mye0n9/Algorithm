import sys
from collections import deque

def get_cnt(N, K):
    queue = deque([(N, 0)]) 
    visited = set([N]) 
    
    while queue:
        current, cnt = queue.popleft()
        
        if current == K:
            return cnt
        
        for next in (current + 1, current - 1, current * 2):
            if 0 <= next <= 100000 and next not in visited:
                visited.add(next)
                queue.append((next, cnt + 1))

N, K = map(int, sys.stdin.readline().strip().split())
print(get_cnt(N, K))
