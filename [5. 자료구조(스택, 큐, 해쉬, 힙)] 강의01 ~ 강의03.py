### [05. 자료구조(스택, 큐, 해쉬, 힙) - 01] 가장 큰 수 (스택)

'''
스택이란?
데이터 간 순서를 약속하는 것. 어떤 물건이 차곡차곡 쌓여있는 것.
보통 쌓여있는 접시에서는 맨 위에것부터 쓸 것이다. 새걸넣어도 맨위이다.
접시를 넣는것도 빼는것도 맨위에서 수행한다.
스택 데이터도 마찬가지다. 맨끝에 항상 데이터를 더하거나 뺀다. 
즉, 스택은 LIFO(last in first out)이다. 그러므로 맨 뒤에 데이터에 접근할 수 있어야 한다.

스택특징
자료형은 없고, deque를 이용해 스택을 쓴다.
※ deque: 맨 앞과 뒤에 데이터를 삽입하고 삭제할 수 있게 해주는 자료형

추가는 append
접근은 [-1]
삭제는 pop()

꿀팁: if list명 이라고했을 때, 리스트 비어있으면 거짓. 리스트 뭐라도 있으면 참 출력
'''


# 답안

num, m = map(int, input().split())

# 위에서 숫자로 받아서(m 때문), str로 바꿔준다. 그후 한개한개씩을 int로 list화 한다. (중요)
num = list(map(int, str(num)))
stack=[]

for x in num:
    # stack(리스트이름)을 조건에 걸 경우: 비었으면 False, 뭐라도 들어가 있으면 True
    while stack and m>0 and stack[-1]<x:
        stack.pop()
        m-=1
    stack.append(x)
if m!=0:
    stack=stack[:-m]
for x in stack:
    print(x, end='')



### [05. 자료구조(스택, 큐, 해쉬, 힙) - 02] 쇠막대기 (스택)


### [05. 자료구조(스택, 큐, 해쉬, 힙) - 03] 후위 표기식 만들기 (스택)
'''
문제 설명:
스택으로 기호들을 넣는다.
만약 연산처리가 현재 다루는 연산보다 빠르거나 같다면 Pop. 그게 아니면 쌓는 과정을 반복
'''
# 
from collections import deque

problem = '3+5*2/(7-2)'

answer = []
stack = deque([])

for i in problem:
    if i.isdecimal():
        answer.append(i)

    else:
        if stack:
            if (stack[-1] == '*') or (stack[-1] == '/'):
                answer.append(stack.pop())
                stack.append(i)
            if (stack[-1] == ')'):
                stack.pop()
                while stack[-1] == '(':
                    answer.append(stack.pop())
            else:
                stack.append(i)
        else:
            stack.append(i)

for _ in range(len(stack)):
    answer.append(stack.pop())
    
print(answer)



# 답안
a=input()
stack=[]
res=''

for x in a:
    # 숫자면 그냥 출력
    if x.isdecimal():
        res+=x
    # 연산자일 경우 조건문 생성
    else:
        if x=='(':
            stack.append(x)
        elif x=='*' or x=='/':
            while stack and (stack[-1]=='*' or stack[-1]=='/'):
                res+=stack.pop()
            stack.append(x)
        elif x=='+' or x=='-':
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.append(x)
        elif x==')':
            while stack and stack[-1]!='(':
                res += stack.pop()
            stack.pop()

while stack:
    res += stack.pop()
