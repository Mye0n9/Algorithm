import sys

l = int(sys.stdin.readline())
val = sys.stdin.readline()
res = 0
for num, word in enumerate(val):
    if num < l:
        res+=((ord(word)-96)*(31**num))
print(res)
# 50 점 