import sys

n = int(input())
towerList = list(map(int, input().split()))
stack = []

for i in range(n):
    h = towerList[i]
    if stack:
        while stack:
            if stack[-1][0]<h:
                stack.pop()
                if not stack:
                    print(0, end ='')
            elif stack[-1][0]>h:
                print(stack[-1][1]+1, end ='')
                break
            else:
                print(stack[-1][1]+1, end = '')
                stack.pop()
                break
        stack.append([h, i])
    else:
        print(0, end = '')
        stack.append([h, i])