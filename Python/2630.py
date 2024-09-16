import sys

sys.setrecursionlimit(10000)

blue = 0
white = 0

def mat_division(mat, size):
    global blue
    global white
    # change to 1d array
    tmp = []
    for element in mat:
        tmp+=element

    # count whether the section is full with white or blue
    if tmp.count(0)==size**2:
        white+=1
    elif tmp.count(1)==size**2:
        blue+=1
    else:
        # if not slice it with four different sizes
        dx = [0, size//2]
        dy = [0, size//2]
        for x in dx:
            for y in dy:
                tmp = [mat[i][y:y+size//2] for i in range(x,x+size//2)]
                mat_division(tmp,size//2)

n = int(sys.stdin.readline().strip())
mat = []
for _ in range(n):
    mat.append(list(map(int,sys.stdin.readline().strip().split())))

tmp = []
for i in mat:
    tmp += i

mat_division(mat, n)
print(white)
print(blue)