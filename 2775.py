import sys

def get_ppl(k,n,idx,floor):
    if k == idx:
        print(floor[n-1])
        return
    else:
        idx+=1
        for i in range(1,len(floor)):
            floor[i] = floor[i]+floor[i-1]
        get_ppl(k,n,idx,floor)

def each_trial(k,n):
    floor = [i for i in range(1,n+1)]
    get_ppl(k,n,0,floor)
    
itr = int(sys.stdin.readline())
for _ in range(itr):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    each_trial(k,n)

