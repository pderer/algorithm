'''
N <= 10000 이기 때문에 브루트포스 가능
2초 -> 20,000,000 * 2 까지의 연산 가능
프로토 타이핑을 해보고 10000을 직접 넣은 다음, 결과값을 확인한다.
2,666,799가 나오므로 가능함
'''

n = int(input())
num = 0
count = 0
while True:
    num += 1
    if '666' in str(num):
        count += 1
    if count == n:
        break
print(num)