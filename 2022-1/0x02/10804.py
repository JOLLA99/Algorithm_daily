card = [i for i in range(21)]

for _ in range(10):
    a, b =map(int, input().split())
    #뒤집기
    for i in range((b-a+1)//2):
        temp = card[b-i]
        card[b-i]=card[a+i]
        card[a+i]=temp
    
for i in range(1, 21):
    print(card[i], end=' ')