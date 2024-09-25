import sys
import re

equation = sys.stdin.readline().strip()
digits = list(map(int,re.findall("[0-9]+",equation)))

notations = [i for i in equation if not(str.isdigit(i))]

if '-' not in notations:
    pos = len(digits)
else:
    pos = notations.index('-')

print(sum(digits[:pos+1])-sum(digits[pos+1:]))