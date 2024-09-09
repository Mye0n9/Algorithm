# 작성한 코드는 시간초과로 실패
# 왜 그러는지 확인 필요할듯

# import sys

# itr = int(sys.stdin.readline().strip())

# idx = 1

# arr = []
# res = []

# check = 0

# for _ in range(itr):
#     target = int(sys.stdin.readline().strip())

#     while (target not in arr) and (idx <= itr):
#         arr.append(idx)
#         res.append('+')
#         idx+=1

#     if arr[-1] == target:
#         arr.pop()
#         res.append('-')
#     else:
#         check = 1
#         break

# if check:
#     print('NO')
# else:
#     for result in res:
#         print(result)

count = 1
temp = True
stack = []
op = []

N = int(input())
for i in range(N):
    num = int(input())
    # num이하 숫자까지 스택에 넣기
    while count <= num:
        stack.append(count)
        op.append('+')
        count += 1

    # num이랑 스택 맨 위 숫자가 동일하다면 제거
    if stack[-1] == num:
        stack.pop()
        op.append('-')
    # 스택 수열을 만들 수 없으므로 NO
    else:
        temp = False
        break

# 스택 수열을 만들수 있는지 여부에 따라 출력 
if temp == False:
    print("NO")
else:
    for i in op:
        print(i)