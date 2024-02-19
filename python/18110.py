n = int(input())

def round2(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if n == 0:
    print(0)
else:
    ratings = []
    for _ in range(n):
        ratings.append(int(input()))

    ratings.sort()

    exclude = round2(n * 0.15)

    new_ratings = ratings[exclude:n-exclude]

    print(int(round2(sum(new_ratings)/(len(new_ratings)))))