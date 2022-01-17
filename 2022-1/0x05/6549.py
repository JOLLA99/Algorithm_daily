from collections import deque
import sys

while True:
    number = list(map(int, sys.stdin.readline().split()))
    n = number.pop(0)

    if n == 0:
        break
    
    stack = deque()
    answer = 0

    for i in range(n):
        while len(stack)!=0 and number[i]<number[stack[-1]]:
            tmp = stack.pop()

            if len(stack) == 0:
                width = i
            else:
                width = i - stack[-1]-1
            answer = max(answer, width*number[tmp])


        stack.append(i)

    while len(stack)!=0:
        tmp = stack.pop()

        if len(stack) == 0:
            width = n
        else:
            width = n - stack[-1]-1
        answer = max(answer, width*number[tmp])
    
    print(answer)
