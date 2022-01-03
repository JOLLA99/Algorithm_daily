import sys
input = sys.stdin.readline

# 입력 값과 스택 리스트
n = int(input())
stack=[]

def push(x):
    stack.append(x)

def pop():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack.pop())

def size():
    print(len(stack))

def empty():
    if(len(stack)==0):
        print(1)
    else:
        print(0)

def top():
    if(len(stack)==0):
        print(-1)
    else:
        print(stack[-1])

# n번 반복 시에 맞는 값일 경우에 해당 함수를 호출한다
for i in range(n):
    com = input().split()
    if (com[0]=='push'):
        push(com[1])
    if (com[0]=='pop'):
        pop()
    if (com[0]=='size'):
        size()
    if (com[0]=='empty'):
        empty()
    if (com[0]=='top'):
        top()
