word = input()
counts = [0] * 26

for i, w in enumerate(word):
    if ord(w) - 97 < 0: # 대문자
        counts[ord(w) - 65] += 1
    else: # 소문자
        counts[ord(w) - 97] += 1

dup = 0
index = 0
max = max(counts)

for i, count in enumerate(counts):
    if count == max:
        dup += 1
        index = i


if dup > 1:
    print("?")
else:
    print(chr(index + 65))