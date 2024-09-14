# import sys

# sys.setrecursionlimit(10000)

# n, m = map(int,sys.stdin.readline().strip().split())

# relation = {key + 1: [] for key in range(n)}

# for _ in range(m):
#     p1, p2 = map(int, sys.stdin.readline().strip().split())
#     relation[p1].append(p2)
#     relation[p2].append(p1)

# pool = [0 for _ in range(n)]
# visited = [0 for _ in range(n)]

# def find_visited(n):
#     visited[n-1] = 1
#     if 0 not in visited:
#         return sum(pool)
#     else:
#         for idx in range(n):
#             if visited[idx] == 0:
#                 pool[idx]+=1 # 방문하지 않았다면 1씩 증가
        
#         for i in relation[n]:
#             visited[i-1] =1 # 방문 했다면 방문했다고 표시

#         for pos in relation[n]:
#             find_visited(pos+1) # 다음 이웃 찾아서 방문 시작

# res = []

# for num in range(n):
#     res.append(find_visited(num+1))
# print(res)
        

         
