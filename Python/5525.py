import sys
N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

cnt, idx, res = 0,0,0

while idx < (M-1):
    if S[idx:idx+3] == 'IOI':
        idx+=2
        cnt +=1
        if cnt == N:
            res+=1
            cnt -=1
    else:
        idx+=1
        cnt=0
print(res)