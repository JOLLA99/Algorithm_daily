n = int(input())
l = list(map(int, input().split()))
l.sort()
sum=0

for i in range(n):
    for j in range(i+1):
        sum += l[j]

print(sum)