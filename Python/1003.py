import sys

# 0: 1 0
# 1: 0 1
# 2: 1 1
# 3: 1 2
# 4: 2 3
# 5: 3, 5

itr = int(sys.stdin.readline().strip())
for _ in range(itr):
    n = int(sys.stdin.readline().strip())
    zero, one = 1, 0
    for _ in range(n):
        zero, one = one, zero+one
    print(zero, one)
