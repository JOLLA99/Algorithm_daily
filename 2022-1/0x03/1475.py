n = input()

card=[0]*10
card_spc=0

for i in n:
    if(i=='6' or i=='9'):
        card_spc+=1
    else:
        card[int(i)]+=1

if(card_spc%2==0):
    card_spc = card_spc//2
else:
    card_spc =card_spc//2+1

card[6]=card_spc
print(max(card))