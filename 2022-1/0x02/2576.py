num=[]
for _ in range(7):
    a = int(input())
    if a%2!=0:
        num.append(a)

if num:
    print(sum(num))
    print(min(num))
else:
    print(-1)