
n =  int(input())
tel = list(map(int, input().split()))
y=m=0

for i in tel:
    y+=(i//30+1)*10
    m+=(i//60+1)*15
if m == y:
    print("Y", "M", y)
elif m<y:
    print("M", m)
else:
    print("Y", y)
