from math import factorial
#예제 입력 받음
n, k = map(int, input().split())
sum = factorial(n) // (factorial(k) * factorial(n-k))
print(sum)