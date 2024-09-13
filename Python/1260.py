import sys

sys.setrecursionlimit(10000)

def dfs(point):
    print(point, end = ' ')
    visited_dfs[point-1] = True
    for n_point in graph[point]:
        if visited_dfs[n_point-1] == False:
            dfs(n_point)

def bfs(queue):
    point = queue.pop(0)
    print(point, end= ' ')
    visited_bfs[point-1] = True
    for n_point in graph[point]:
        if (visited_bfs[n_point-1] == False) and (n_point not in queue):
            queue.append(n_point)
    if queue == []:
        return
    else:
        bfs(queue)
    

n, m, v = map(int, sys.stdin.readline().strip().split())

graph = {key+1 : [] for key in range(n)}

visited_dfs = [False for key in range(n)]
visited_bfs = [False for key in range(n)]

for _ in range(m):
    v_1, v_2 = map(int,sys.stdin.readline().strip().split())
    graph[v_1].append(v_2)
    graph[v_1] = sorted(graph[v_1])
    graph[v_2].append(v_1)
    graph[v_2] = sorted(graph[v_2])

dfs(v)
print()
bfs([v])
