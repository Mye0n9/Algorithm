import sys

itr = int(sys.stdin.readline().strip())

# all cases

cases = [1,2,4]
for i in range(8):
    cases.append(cases[i]+cases[i+1]+cases[i+2])

for _ in range(itr):
    num = int(sys.stdin.readline().strip())
    print(cases[num-1])
    