import sys

T = int(input())

for _ in range(T):
    stack = []

    s = sys.stdin.readline().rstrip()

    flag = True

    for j in range(len(s)):
        if s[j]=='(':
            stack.append(s[j])
        else:
            if stack and s[j]==')' and stack[-1]=='(':
                stack.pop()
            elif not stack:
                flag = False
                break
    
    if not stack and flag:
        print('YES')
    else:
        print('NO')
    