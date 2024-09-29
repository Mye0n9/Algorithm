import sys

arr = [1,3]

num = int(sys.stdin.readline().strip())

if num == 1:
    print(arr[0])
elif num == 2:
    print(arr[1])
else:
    for _  in range(num-2):
        arr.append(arr[len(arr)-1] + 2 * arr[len(arr)-2])
    print(arr[-1]%10007)