n = int(input())

for i in range(n):
    blanks = " " * (n-i-1)
    print(blanks + "*" * (i+1))