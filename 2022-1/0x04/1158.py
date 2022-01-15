n, k = map(int, input().split())
s = [i for i in range(1, n+1)]
answer = []
num = 0 

for i in range(n):
    num += k-1
    if num >= len(s):
        num = num % len(s)
    
    answer.append(str(s.pop(num)))

print("<",", ".join(answer[:],">", sep=''))
