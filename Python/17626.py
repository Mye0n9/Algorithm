# import sys

# sys.setrecursionlimit(100000)

# possible_set = []

# def get_possible_cnt(num, cnt):
#     if num == 0:
#         possible_set.append(cnt)
#         return
#     else:
#         cnt+=1
#         max_point = int(num**(0.5))
#         for n_num in range(max_point,0,-1):
#             next_point = num - int(n_num**2)
#             get_possible_cnt(next_point,    cnt)



# num = int(sys.stdin.readline().strip())
# get_possible_cnt(num,0)
# print(min(possible_set))

import math
 
n = int(input())
dp = [0] * (n + 1)
dp[0], dp[1] = 0, 1
 
for i in range(2, n + 1):
    if i == int(math.sqrt(i)) ** 2:
        dp[i] = 1
    else:
        dp[i] = i
 
for i in range(2, n + 1):
    for j in range(1, int(math.sqrt(i)) + 1):
        dp[i] = min(dp[i], dp[j * j] + dp[i - j * j])
print(dp[n])