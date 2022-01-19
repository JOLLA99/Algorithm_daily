import sys
input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break
    
    stack = []

    for i in range(len(s)):
        if s[i]== "(" or s[i] == "{":
            stack.append(s[i])
        elif stack and (s[i]== ")" or s[i] == "}"): #stack은 있지만 닫힌 괄호 나오는 경우
            if s[i] == ")" and stack[-1] == "(":
                stack.pop()
            elif s[i] == "}" and stack[-1] == "{":
                stack.pop()
            else:
                flag= False
        
        elif not stack and (s[i]== ")" or s[i] == "}"):
            flag = False

    if flag and not stack:
        print('yes')
    else:
        print('no')