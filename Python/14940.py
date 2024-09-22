import sys
from collections import deque

sys.setrecursionlimit(10000)

N, M = map(int,sys.stdin.readline().strip().split())
# N:세로
# M: 가로

mat = []

visited = [[-1]*M for _ in range(N)]

s_point = []
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for row in range(N):
    tmp = list(map(int,sys.stdin.readline().strip().split()))
    if 2 in tmp:
        s_point = [row,tmp.index(2)]
    mat.append(tmp)

# BFS
def bfs_shortest(points):
    queue = deque()
    queue.append(points)

    # print(points[0],points[1])

    visited[points[0]][points[1]] = 0

    while queue:
        r,c = queue.popleft()

        for idx in range(4):
            nr, nc = dr[idx] + r, dc[idx] + c

            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == -1:
                if mat[nr][nc] == 0: 
                    visited[nr][nc] = 0
                elif mat[nr][nc] == 1:
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append([nr,nc])

bfs_shortest(s_point)

for i in range(N):
    for j in range(M):
        if mat[i][j] == 0:
            print(0, end=' ')
        else:
            print(visited[i][j], end=' ')
    print()
