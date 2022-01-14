from sys import stdin 

s = stdin.readline().strip()
num = int(input()) #명령어 개수
cursor = len(s)

for i in stdin:
    if i[0]=='L':
        if not cursor==0:
            cursor-=1
    elif i[0]=='D':
        if not cursor==len(s):
            cursor+=1
    elif i[0]=='B':
        if not cursor==0:
            s = s[0:cursor-1]+s[cursor:]
        else: continue
    elif i[0]=='P':
        s = s[0:cursor-1]+i[2]+s[cursor:]

print(s)