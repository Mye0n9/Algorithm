import sys

# seems wrong need to be modified.

def check_intersect(point,wires,intersect):
    for wire in wires:
        if (point[0] > wire[0]) and (point[1] < wire[1]):
            intersect += 1
        if (point[0] < wire[0]) and (point[1] > wire[1]):
            intersect +=1
    wires.append(point)
    return intersect, wires

itr_one = int(sys.stdin.readline())

for _ in range(itr_one):
    itr_two = int(sys.stdin.readline())
    wires = []
    intersect = 0
    for _ in range(itr_two):
        point = tuple(map(int,sys.stdin.readline()[:-1].split()))
        intersect, wires = check_intersect(point,wires,intersect)
    print(intersect)