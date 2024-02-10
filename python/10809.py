word = input()

positions = [-1] * 26

for i, w in enumerate(word):
    if positions[ord(w) - 97] == -1:
        positions[ord(w) - 97] = i

for pos in positions:
    print(pos, end=" ")