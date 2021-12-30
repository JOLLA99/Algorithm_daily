#동전 갯수와 값 입력
n, k = map(int, input().split())

coin = []
#동전의 가치 입력
for _ in range(n):
    coin.append(int(input()))

count=0
i = n-1

while k !=0:
    count += k//coin[i]
    k %= coin[i]
    i-=1
    
print(count)

