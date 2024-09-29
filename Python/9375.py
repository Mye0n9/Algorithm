import sys

for _ in range(int(sys.stdin.readline().strip())):
    c_list = {}
    for _ in range(int(sys.stdin.readline().strip())):
        _, t = sys.stdin.readline().strip().split()

        if t in c_list.keys():
            c_list[t]+=1
        else:
            c_list[t] = 2
    res = 1
    for i in (c_list.values()):
        res *= i
    print(res-1)
    