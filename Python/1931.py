import sys

N = int(sys.stdin.readline().strip())
whole_table = []

for _ in range(N):
    whole_table.append(list(map(int,sys.stdin.readline().strip().split())))

whole_table.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end_time = whole_table[0][1]
for i in range(1,N):
    if whole_table[i][0] >= end_time:
        cnt+=1
        end_time = whole_table[i][1]
print(cnt)