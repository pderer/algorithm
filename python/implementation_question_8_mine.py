strings = input()

alphabet = []
sum = 0

for string in strings:
    try:
        sum += int(string)
    except ValueError:
        alphabet.append(string)

alphabet.sort()
result = ''.join(alphabet)
print(result + str(sum))