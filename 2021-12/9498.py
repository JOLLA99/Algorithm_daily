score = int(input())

if score>=90 and score<=100:
    sum = 'A'
elif score>=80 and score<90:
    sum = 'B'
elif score>=70 and score<80:
    sum = 'C'
elif score>=60 and score<70:
    sum = 'D'
else:
    sum = 'F'

print(sum)