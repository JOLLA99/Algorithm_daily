from math import factorial

T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    bridge = factorial(b) // (factorial(a) * factorial(b-a))
    print(bridge)