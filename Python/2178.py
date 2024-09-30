import sys
from collections import deque

queue = deque([])

N, M = map(int,sys.stdin.readline().strip().split())

mat = []

for _ in range(N):
    tmp = []
    usr_input = sys.stdin.readline().strip()
    for i in usr_input:
        tmp.append(int(i))
    mat.append(tmp)

visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

queue.append([0, 0]) # r, c, cnt

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


while queue[0][0] != N-1 or queue[0][1] != M-1:
    r, c = queue.popleft()
    cnt = visited[r][c] +1
    for idx in range(4):
        nr = r + dr[idx]
        nc = c + dc[idx]
        if (nr >= 0) and (nr < N) and (nc >= 0) and (nc < M) and visited[nr][nc] == 0 and mat[nr][nc]==1:
            queue.append([nr,nc])
            visited[nr][nc] = cnt

print(visited[N-1][M-1])