import sys

N, M = map(int,sys.stdin.readline().strip().split())

tree_list = list(map(int,sys.stdin.readline().strip().split()))

max_h = max(tree_list)
min_h = 0

while min_h <= max_h:
    point = (min_h+max_h)//2

    log = 0
    for tree in tree_list:
        if tree > point:
            log+=tree-point
    
    if log>=M:
        min_h = point + 1
    else:
        max_h = point -1
print(max_h)