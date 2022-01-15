k = int(input())
num = []
for _ in range(k):
    n = int(input())

    if n==0:
        num.pop()
    else:
        num.append(n)

print(sum(num))

