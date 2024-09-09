import sys

n, k = map(int, sys.stdin.readline().strip().split())

account = dict()
for _ in range(n):
    website, pw = sys.stdin.readline().strip().split()
    account[website] = pw

for _ in range(k):
    target = sys.stdin.readline().strip()
    print(account[target])