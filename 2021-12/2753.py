year = input()
year = int(year)

if year%4==0 and year%100!=0 or year%400==0:
        num = 1
else:
        num=0

print(num)