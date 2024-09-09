import sys

itr = int(sys.stdin.readline().strip())

s = []

for _ in range(itr):
    command= sys.stdin.readline().strip()
    if command not in ['all','empty']:
        command, value = command.split()
        value = int(value)

    if command == "add":
        if value not in s:
            s.append(value)
    elif command == "remove":
        if value in s:
            s.remove(value)
    elif command == "check":
        if value in s:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if value in s:
            s.remove(value)
        else:
            s.append(value)
    elif command == "all":
        s = [i for i in range(1,21)]
    elif command == "empty":
        s = []