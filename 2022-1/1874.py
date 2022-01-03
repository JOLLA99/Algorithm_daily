
n = int(input())

a =[]
s = [] # 새로운 수열 담을 리스트
count=1
temp = True

# num 리스트 안에 모두 저장
for i in range(n):
    num = int(input())
    while count <= num:
        s.append(count)
        a.append('+')
        count+=1
    if s[-1]==num:
        s.pop()
        a.append('-')
    else:
        temp = False
      

if temp == False:
    print("No")
else:
    for i in a:
        print(i)


