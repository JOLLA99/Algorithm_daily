import sys

s = sys.stdin.readline().rstrip()
stack = []
result = 0 

for i in range(len(s)):
    
    if s[i] == '(':
        stack.append(s[i])
    else:
        if s[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result +=1

print(result)
    
