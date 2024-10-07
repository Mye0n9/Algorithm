import sys

sys.setrecursionlimit(1000000)

size = int(sys.stdin.readline())

mat = [list(sys.stdin.readline().strip()) for _ in range(size)]
visited = [[False] * size for _ in range(size)]

dr = [1,-1,0,0]
dc = [0,0,1,-1]

sector = 0
sector_two = 0

def dfs (r,c):
    visited[r][c] = True
    current_color = mat[r][c]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if (0<=nr<size)and (0<=nc<size):
            if visited[nr][nc] == False:
                if mat[nr][nc] == current_color:
                    dfs(nr, nc)

for i in range(size):
    for j in range(size):
        if visited[i][j] == False:
            dfs(i,j)
            sector+=1

for i in range(size):
    for j in range(size):
        if mat[i][j] == 'G':
            mat[i][j] = 'R'

visited = [[False] * size for _ in range(size)]

for i in range(size):
    for j in range(size):
        if visited[i][j] == False:
            dfs(i,j)
            sector_two+=1

print(sector, sector_two)