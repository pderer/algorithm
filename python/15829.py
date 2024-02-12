l = int(input())
strings = input()

r = 31
m = 1234567891
result = 0

for i, s in enumerate(strings):
    result += ((ord(s) - 96) * r ** i) % m
print(result % m)