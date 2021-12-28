

#맨처음 입력 받는 수
n = int(input())

for i in range(1, n+1):
    num = sum(map(int, str(i))) #각 자리 수를 모두 더해준다
    num_sum = num+i
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)
