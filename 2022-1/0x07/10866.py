N = int(input())

deq = [] # 덱

print_list=[]

for i in range(N):
    sen = list(map(str, input().split()))

    if sen[0]=="push_front":
        deq.insert(0, sen[1])
    elif sen[0]=="push_back":
        deq.append(sen[1])
    elif sen[0]=="pop_front":
        if len(deq)==0:
            # print(-1)
            print_list.append(-1)
        else:
            # print(deq.pop(0))
            print_list.append(deq.pop(0))
    elif sen[0]=="pop_back":
        if len(deq)==0:
            #print(-1)
            print_list.append(-1)
        else:
            #print(deq.pop(-1))
            print_list.append(deq.pop(-1))
    elif sen[0]=="size":
        #print(len(deq))
        print_list.append(len(deq))
    elif sen[0]=="empty":
        if len(deq)==0:
            #print(1)
            print_list.append(1)
        else:
            #print(0)
            print_list.append(0)
    elif sen[0]=="front":
        if len(deq)==0:
            #print(-1)
            print_list.append(-1)
        else:
            # print(deq[0])
            print_list.append(deq[0])
    elif sen[0]=="back":
        if len(deq)==0:
            #print(-1)
            print_list.append(-1)
        else:
            # print(deq[-1]) 
            print_list.append(deq[-1])
    

for i in range(len(print_list)):
    print(print_list[i])
