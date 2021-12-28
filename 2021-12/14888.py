import sys
s1 = sys.stdin.readline().strip().upper()
s2 = sys.stdin.readline().strip().upper()

len1 = len(s1)
len2 = len(s2)
matrix = [[0]*(len2+1)for _ in range(len1+1)]

for i in range(1, len1+1):
    for j in range(1, len2+1):
        
