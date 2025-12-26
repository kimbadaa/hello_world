# No.3052 나머지

n = []

for i in range(10):
    a = int(input())
    b = a % 42
    n.append(b)

s = set(n)
print(len(s))



# No. 2577 숫자의 개수

a = int(input())
b = int(input())
c = int(input())
result = list(str(a * b * c))

for i in range(10):
    print(result.count(str(i)))



# No. 8958 OX퀴즈

a = int(input())

for i in range(a):
    k = input()
    score = 0
    total = 0
    for j in range(len(k)):
        if k[j] == 'O':
            score += 1
            total += score
        else:
            score = 0

    print(total)



# No. 1978 소수찾기

n = int(input())

n_list = list(map(int, input().split())) #split() 공백 기준으로 나눔

for i in n_list:
    if i == 1:
        n -= 1
    for j in range(2, i):
        if i % j == 0:
            n -= 1
            break
print(n)



# No. 2750 수 정렬하기

n = int(input())

n_list = []

for i in range(n):
    n_list.append(int(input()))

for i in sorted(n_list): #sorted()리스트를 정렬해서 새 리스트로
    print(i)



# No. 2798 블랙잭
from itertools import combinations  #iterable에서 원소 개수가 r개인 조합 뽑기

n, m = map(int, input().split())
cards  = list(map(int, input().split()))

total = 0
for i in combinations(cards, 3):
    if total < sum(i) <= m:
        total = sum(i)

print(total)



# No. 2292 벌집

n = int(input())

layer = 1
number = 1

while n > number:
    number += 6 * layer
    layer += 1


print(layer)

