def find(n):
    number = n
    
    for i in list(str(n)):
        number += int(i)
    return number

non_self_numbers = []

for i in range(1, 10001):
    num = find(i)
    non_self_numbers.append(num)

for i in range(1, 10001):
    if i in non_self_numbers:
        pass
    else:
        print(i)