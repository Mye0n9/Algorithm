import heapq
import sys

heap = []

for _ in range(int(sys.stdin.readline().strip())):
    tmp = int(sys.stdin.readline().strip())
    if tmp == 0:
        if heap == []:
            print(0)
        else:
            print(heapq.heappop(heap)*(-1))
    else:
        heapq.heappush(heap,tmp*(-1))
