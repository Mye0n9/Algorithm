import sys

def check_loop(sentence):
    res = 0
    for i in range(len(sentence)-2):
        if sentence[i:i+3] == 'for':
            res += 1
    for i in range(len(sentence)-4):
        if sentence[i:i+5] == 'while':
            res += 1
    return res

itr = int(sys.stdin.readline())
cnt_arr = []
for _ in range(itr):
    sentence = sys.stdin.readline()[:-1]
    cnt_arr.append(check_loop(sentence=sentence))
print(max(cnt_arr))