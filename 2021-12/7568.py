
#인원 입력
n = int(input())

data=[] #개인 데이터 저장용 리스트
score=[]

#사람 몸무게와 키 입력
for i in range(n):
    a, b = map(int, input().split())
    data.append((a, b))

for i in range(n):
    count=0
    for j in range(n):
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count+=1
    score.append(count+1)

for i in score:
    print(i, end=" ")

