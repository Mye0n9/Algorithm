import sys, heapq

abs_heap = []

for _ in range(int(sys.stdin.readline().strip())):
    num = int(sys.stdin.readline().strip())
    if num:
        heapq.heappush(abs_heap,(abs(num),num))
    else:
        if abs_heap:
            print(heapq.heappop(abs_heap)[1])
        else:
            print(0)