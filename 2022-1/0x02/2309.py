num = []
for _ in range(9):
    num.append(int(input()))
# 전체 더한 값에서 두명 분을 빼서 100을 찾으면 됨
total = sum(num)

for i in range(9):
    for j in range(i+1, 9):
        if total - (num[i]+num[j])==100:
            n1, n2 = num[i], num[j]

            num.remove(n1)
            num.remove(n2)
            num.sort()

            for i in range(len(num)):
                print(num[i])
            break
    if len(num)<9:
        break

