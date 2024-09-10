import sys

num = int(sys.stdin.readline().strip())

arr = [1,2]

for i in range(num-2):
    arr.append(arr[i] + arr[i+1])

if num == 1:
    print(1)
elif num ==2:
    print(2)
else:
    print(arr[len(arr)-1] % 10007)