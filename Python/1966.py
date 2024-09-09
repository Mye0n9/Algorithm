import sys

itr = int(sys.stdin.readline().strip())


for _ in range(itr):
    pages, target = map(int, sys.stdin.readline().split())
    importances = list(map(int, sys.stdin.readline().split()))

    result = 1
    while importances:
        if importances[0] < max(importances):
            importances.append(importances.pop(0))
        else:
            if target == 0:
                break
            
            importances.pop(0)
            result+=1
        target = target -1 if target > 0 else len(importances) - 1
    print(result)
        