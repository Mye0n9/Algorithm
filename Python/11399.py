import sys
_ = sys.stdin.readline()

arr = sorted(list(map(int, sys.stdin.readline().strip().split())))
for i in range(len(arr)):
    if i >0:
        arr[i] = arr[i] + arr[i-1]
print(sum(arr))