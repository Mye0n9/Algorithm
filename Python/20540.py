import sys

mbti = sys.stdin.readline()[:-1]

mbti_dict = {
    'I':'E',
    'N':'S',
    'F':'T',
    'J':'P'
}
inverted_dict = {value: key for key, value in mbti_dict.items()}

res = ""
for symbol in mbti:
    if symbol in mbti_dict.keys():
        res+=mbti_dict[symbol]
    elif symbol in inverted_dict.keys():
        res+=inverted_dict[symbol]
    else:
        print("error")
print(res)