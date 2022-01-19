import sys

N = int(input())
count = 0 

for _ in range(N):
    sen = sys.stdin.readline().rstrip()
    stack = []
    
    for j in range(len(sen)):
        if stack:
            if sen[j] == stack[-1]:
                stack.pop()
            else:
                stack.append(sen[j])
        
        else:
            stack.append(sen[j])
    
    if not stack:
        count+=1
            

print(count)
    

