import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    s = list(input().strip())
    left, right=[]
    for i in s:
        if i == '<':
            if left:
                right.append(left.pop())
        elif i == '>':
            if right:
                left.append(right.pop())
        elif i =='-':
            if left:
                left.pop()
        else:
            left.append(i)
    left.extend(reversed(right))
    print(''.join(left))