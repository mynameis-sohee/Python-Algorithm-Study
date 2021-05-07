### [05. 자료구조(스택, 큐, 해쉬, 힙) - 04] 후위(postfix) 연산(스택)
'''
문제 핵심: 부호를 나눠서 if 문을 작성
답안 참고하여 문제 풀이 진행(문제 풀이완료) -재풀이 필요
'''
# 풀이과정
problem = '352+*9-'
answer = ''
stack = []
for x in problem:
    if x.isdecimal():
        stack.append(int(x))
    else:
        if x=='+':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2+n1)
        if x=='-':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2-n1)
        if x=='*':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2*n1)
        if x=='/':
            n1=stack.pop()
            n2=stack.pop()
            stack.append(n2/n1)

print(stack[0])




### [05. 자료구조(스택, 큐, 해쉬, 힙) - 05] 공주구하기(큐)

'''
큐 자료구조란?
어떤 데이터는 뒤로 넣고, 앞에서 데이터를 꺼낸다.
마치 병원 대기줄처럼 말이다. 들어가는 순서대로 나오는 것이다.
FIFO 형식이다.

큐를 사용할 땐, deque를 사용한다.
뒤에서는 append와 pop을, 앞에서 넣을땐 appendleft 앞에서 꺼낼땐 popleft 를 사용한다.
큐 사용 시 튜플을 활용한다.
'''


'''
문제풀이: 스스로 진행, 아이디어 강의 착안
'''

# 풀이과정
n=8
k=3

_list_= list(range(1, n+1) )

# 앞뒤로 append, pop 할거니까 자료구조 변경
# popleft는 deque에서만 가능

from collections import deque
_list_ = deque(_list_)


while len(_list_)>1:
    for _ in range(k-1):
        _list_.append(_list_.popleft())
    _list_.popleft()

print(_list_[0])



### [05. 자료구조(스택, 큐, 해쉬, 힙) - 06] 응급실(큐)
'''
특이사항: enumerate (순서대로 튜플에 저장하는 함수) 활용
'''

# 풀이과정
n = 6
m = 0

# 라벨을 붙여주는 함수: enumerate. 순서대로 튜플에 저장
dag_list = [(0,60), (1,60), (2,90), (3,60), (4,60), (5,60)]

from collections import deque
dag_list = deque(dag_list)


cnt = 0

while True:
    max_num = max(dag_list, key= lambda x : x[1])
    if max_num != dag_list[0]:
        dag_list.append(dag_list.popleft())
    else:
        answer = dag_list.popleft()
        answer = answer[0]
        cnt += 1

        if answer == m:
            print(cnt)
            break




### [05. 자료구조(스택, 큐, 해쉬, 힙) - 07] 교육과정설계(큐)

'''
문제 정의
과목: ABCDEFG
필수: C->B->A
'''

# 풀이과정
from collections import deque


must_class = ['C','B','A']
n = 3

for i in range(n):

    ttl_class = deque(list(input().split()))
    answer = []

    while len(answer) < len(must_class):
        cla = ttl_class.popleft()
        if cla in must_class:
            answer.append(cla)

    if ''.join(answer) == ''.join(must_class):
        print('#{} YES'.format(i+1)) 
    else:
        print('#{} NO'.format(i+1))    
