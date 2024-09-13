import sys

pool = []

for _ in range(3):
    pool.append(int(sys.stdin.readline().strip()))

print(pool[0]+pool[1]-pool[2])
print(int(str(pool[0])+str(pool[1]))-pool[2])