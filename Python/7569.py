import sys
from collections import deque

dr = [-1, 0, 1, 0, 0, 0]
dc = [0, 1, 0, -1, 0, 0]
dz = [0, 0, 0, 0, 1, -1]

M, N, H= map(int, sys.stdin.readline().strip().split())

tray = []

for _ in range(H):
  tmp = []
  for _ in range(N):
    tmp.append(list(map(int, sys.stdin.readline().strip().split())))
  tray.append(tmp)

Q = deque()

for z in range(H):
  for r in range(N):
    for c in range(M):
      if tray[z][r][c] == 1:
        Q.append([z, r, c])

while Q:
  length = len(Q)
  for _ in range(length):
    z, r, c = Q.popleft()

    for i in range(6):
      nr = r + dr[i]
      nc = c + dc[i]
      nz = z + dz[i]


      if nr >= 0 and nr < N and nc >= 0 and nc < M and nz >= 0 and nz < H and tray[nz][nr][nc] == 0:
        tray[nz][nr][nc] = tray[z][r][c] + 1
        Q.append([nz,nr, nc])
        
def get_1d_array(arr):
  tmp = []
  for i in range(len(arr)):
    for j in range(len(arr[i])):
      tmp+=arr[i][j]
  return tmp

one_dim = get_1d_array(tray)
if 0 in one_dim:
  print(-1)
else:
  print(max(one_dim)-1)