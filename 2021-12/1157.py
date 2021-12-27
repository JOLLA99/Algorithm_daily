sen = (input()).upper()
cnt_list=[]

for i in list(set(sen)):
    cnt = sen.count(i)
    cnt_list.append(cnt)

if cnt_list.count(max(cnt_list))>1:
    print("?")
else:
    max_in = cnt_list.index(max(cnt_list))
    print(list(set(sen))[max_in])

