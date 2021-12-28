
def fac(n):
    sum=1
    if n>0:
        sum = n* fac(n-1)
    return sum

n = int(input())
print(fac(n))