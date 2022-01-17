from collections import deque

n = int(input())
number = list(map(int, input().split()))
nge= [-1]*n
stack= deque()

for i in range(n):
    while stack and stack[-1][0] < number[i]:
        tmp, idx = stack.pop()
        nge[idx] = number[i]
    stack.append([number[i], i])


print(*nge)