import sys

def find_num(n, r, c, res):
    if n == 1:
        base = [[0,1],[2,3]]
        return res + base[r][c]
    else:
        gap = 4 ** (n-1)
        if r >= 2 ** (n-1):
            res += 2 * gap
            r -= 2**(n-1)
        if c >= 2**(n-1):
            res += gap
            c -= 2**(n-1)
        return find_num(n-1, r, c, res)
        

n, r, c = map(int, sys.stdin.readline().split())
print(find_num(n,r,c,0))