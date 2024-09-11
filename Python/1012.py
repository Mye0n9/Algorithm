import sys

sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if (0<=nx<m) and (0<=ny<n):
            if mat[ny][nx] == 1:
                mat[ny][nx] = 0
                dfs(nx, ny)

for _ in range(int(sys.stdin.readline())):
    m, n, k = map(int, sys.stdin.readline().strip().split())
    mat = [[0 for _ in range(m)] for _ in range(n)]
    cnt = 0
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().strip().split())
        mat[y][x] = 1
    for x in range(m):
        for y in range(n):
            if mat[y][x] == 1:
                dfs(x,y)
                cnt+=1
    print(cnt)
        