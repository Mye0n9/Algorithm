import sys
from collections import deque

res = sys.maxsize
p_res = 0

N, M = map(int, sys.stdin.readline().strip().split())

visited = [0 for _ in range(N)]
pool = deque([])
connections = {i+1:[] for i in range(N)}

for _ in range(M):
    p1, p2 = map(int,sys.stdin.readline().strip().split())
    connections[p1].append(p2)
    connections[p2].append(p1)

for p in range(N):
    pivot = p
    visited[pivot] = 1
    pool.append(pivot)
    while 0 in visited:
        for n_points in connections[pivot+1]:
            if visited[n_points-1] == 0:
                visited[n_points-1] = visited[pivot]+1
                pool.append(n_points)
        pool.popleft()
        pivot = pool[0]-1
    
    if sum(visited) < res:
        p_res = p+1
        res = sum(visited)
    
    visited = [0 for _ in range(N)]
    pool = deque([])
print(p_res)