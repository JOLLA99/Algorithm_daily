s = int(input()) #테스트 케이스의 수

for i in range(s):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    check = [0 for _ in range(n)]
    check[m]=1

    count=0
    while True:
        if a[0]==max(a):
            count+=1

            if check[0]==1:
                print(count)
                break
            else:
                a.pop(0)
                check.pop(0)
        else:
            a.append(a.pop(0))
            check.append(check.pop(0))




