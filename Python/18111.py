import sys

N, M, B = map(int,sys.stdin.readline().strip().split())

mat = []

for _ in range(N):
    mat += list(map(int,sys.stdin.readline().strip().split()))

time = [0]*257
height = 0

for i in range(257):
    block = B
    for j in mat:
        if j <= i:
            time[i] += i-j
            block -= i-j
        else:
            time[i] += 2*(j-i)
            block+= j-i
    if block >= 0 and time[i] <= time[height]:
        height = i

print(time[height], height)