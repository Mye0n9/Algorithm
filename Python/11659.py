import sys

nums, itr = map(int, sys.stdin.readline().strip().split())
arr = list(map(int, sys.stdin.readline().strip().split()))

for i in range(nums):
    if i != 0:
        arr[i] += arr[i-1]

for _ in range(itr):
    start, end = map(int, sys.stdin.readline().strip().split())
    if start == 1:
        print(arr[end-1])
    else:
        print(arr[end-1]-arr[start-2])