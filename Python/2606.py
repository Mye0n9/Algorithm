# import sys

# computers = int(sys.stdin.readline().strip())
# n_pairs = int(sys.stdin.readline().strip())

# virus_check = [1 if i == 1 else 0 for i in range(1, computers + 1)]

# pairs = {}

# for _ in range(n_pairs):
#     key, value = map(int, sys.stdin.readline().strip().split())
#     if key in pairs.keys():
#         pairs[key].append(value)
#     else:
#         pairs[key] = [value]

# pairs = dict(sorted(pairs.items()))

# for key in pairs.keys():
#     for vals in pairs[key]:
#         if virus_check[key-1] == 1:
#             virus_check[vals-1] = 1

# print(sum(virus_check)-1) 


# Reference
n=int(input()) # 컴퓨터 개수
v=int(input()) # 연결선 개수
graph = [[] for i in range(n+1)] # 그래프 초기화
visited=[0]*(n+1) # 방문한 컴퓨터인지 표시
for i in range(v): # 그래프 생성
    a,b=map(int,input().split())
    graph[a]+=[b] # a에 b 연결
    graph[b]+=[a] # b에 a 연결 -> 양방향
def dfs(v):
    visited[v]=1
    for nx in graph[v]:
        if visited[nx]==0:
            dfs(nx)
dfs(1)
print(sum(visited)-1)