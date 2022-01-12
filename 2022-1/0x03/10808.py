a = input()
alpha=[0]*26

for i in range(a):
    alpha[ord(i)-97] +=1

print(*alpha)