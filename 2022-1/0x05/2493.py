n = int(input())

tL = list(map(int, input().split()))
aL = [0 for _ in range(n)]
stack= []
# 그렇다..

for i in range(n+1, -1, -1):
    if len(stack) == 0:
        stack.append([i, tL[i]])
    else:
        while tL[i]>stack[len(stack)-1][1]:
            tower = stack.pop()
            aL.append[tower[0]] = i+1
            if len(stack)==0:
                break
        
        stack.append([i, tL[i]])

for num in aL:
    print(num, end=" ")
