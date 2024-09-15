import sys

from collections import deque

for _ in range(int(sys.stdin.readline().strip())):
    commands = sys.stdin.readline().rstrip()
    num_element = int(sys.stdin.readline().strip())
    arr = sys.stdin.readline().strip()[1:-1].split(",")

    queue = deque(arr)

    rev, front, back = 0, 0, len(queue)-1
    flag = 0

    if num_element == 0:
        queue = []
        front = 0
        back = 0
    
    for command in commands:
        if command == 'R':
            rev+=1
        elif command == 'D':
            if len(queue) < 1:
                flag = 1
                print("error")
                break
            else:
                if rev%2 ==0:
                    queue.popleft()
                else:
                    queue.pop()
    if flag == 0:
        if rev % 2 ==0:
            print("[" + ",".join(queue) + "]")
        else:
            queue.reverse()
            print("[" + ",".join(queue) + "]")
