import sys

itr, target = map(int,sys.stdin.readline().strip().split())
types = []
for _ in range(itr):
    money = int(sys.stdin.readline().strip())
    if money <= target:
        types.append(money)
types = sorted(types,reverse=True)

cnt = 0
for t in types:
    tmp = target//t
    cnt += tmp
    target -= t * tmp
    if target == 0:
        break
print(cnt)