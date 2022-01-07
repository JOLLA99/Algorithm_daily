



a, b, c = map(int, input().split())

def dec(a,b):
    if b==1:
        return a%c
    else:
        temp = dec(a, b//2)
        if b%2==0:
            return temp*temp%c
        else:
            return temp*temp*a%c

print(dec(a,b))
