def sum(a):
    s = 0 
    for i in range(5):
        s+=a[i]

    num = s//5
    return num

a= [] 
for _ in range(5):
    a.append(int(input()))

a.sort()
print(sum(a))
print(a[2])