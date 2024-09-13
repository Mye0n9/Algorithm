import sys

sys.setrecursionlimit(10000)

n, m = map(int, sys.stdin.readline().strip().split())

visited = [False for _ in range(n)]

def dfs(point):
    visited[point-1] = True
    for n_point in graph[point]:
        if visited[n_point-1] == False:
            dfs(n_point)

graph = {key + 1:[] for key in range(n)}

for _ in range(m):
    v_1, v_2 = map(int,sys.stdin.readline().strip().split())
    graph[v_1].append(v_2)
    graph[v_2].append(v_1)

cnt = 0

for idx in range(n):
    if visited[idx] == False:
        cnt+=1
        dfs(idx+1)
print(cnt)