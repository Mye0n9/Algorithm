# import sys

# heap = []

# for _ in range(int(sys.stdin.readline().strip())):
#     usr_input = int(sys.stdin.readline().strip())
#     if usr_input == 0:
#         if len(heap)==0:
#             print(0)
#         else:
#             print(heap.pop(0))
#     else:
#         heap.append(usr_input)
#         heap = sorted(heap)

import sys
import heapq
input = sys.stdin.readline

min_heap = []

for _ in range(int(input())):
    n = int(input())
    
    if n == 0:
        if len(min_heap):
            print(heapq.heappop(min_heap))
        else:
            print(0)
    else:
        heapq.heappush(min_heap, n)