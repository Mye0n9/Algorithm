import sys

participants = int(sys.stdin.readline())
sizes = sorted(list(map(int,sys.stdin.readline().split())))
t, p = map(int, sys.stdin.readline().split())

# shirt
shirt = 0
for size in sizes:
    if size % t !=0:
        shirt += size//t + 1
    else:
        shirt+=size//t
    print(shirt)

print(shirt)
# pen
print(participants//p,participants % p)