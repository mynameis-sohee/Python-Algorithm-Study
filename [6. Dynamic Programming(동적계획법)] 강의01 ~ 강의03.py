### [06. Dynamic Programming(동적계획법) - 01]  재귀함수를 이용한 이진수 출력
'''
Bottom-up적 동적계획법이란?
만약 문제가 너무 크다면, 작은단위의 문제크기로 바꿔 작은단위의 해를 구한다.
그리고 이걸 다시 조금 더 큰 문제로 적용해 해를 구하는데, 앞단 해를 활용해 답을 구해낸다. (점화식)
아주작은 문제의 해 -> 큰 문제의 해로 구하는거니까, 이런 방법을 Bottom-up적 동적계획법이라고 부른다.
'''

'''
십진수와 이진수
십진수: 우리가 평소 일상적으로 사용하는 것
이진수: 2를 나눴을 때 나오는 나머지값(0 아니면 1) 그 나머지를 계속 출력한다. 나눴을때의 그 값을 역으로 출력하면 된다. 
'''

# 풀이과정
def binary(qu):
    # 나머지
    re = qu % 2
    # 몫
    qu = qu // 2 
    return re, qu

quotient = 11
from collections import deque
answer = deque([])

while quotient > 0:
    if quotient >= 2:
        remainder, quotient = binary(quotient)
        answer.append(remainder)
    else:
        answer.append(quotient)
        while answer:
            print(answer.pop(), end='')
        break



# 답안
'''
핵심: 이 문제는 stack이 적용되는 문제다.
함수는 풀다가 만약 중간에 끊기면 그것들을 마치 stack 처럼 쌓아준다.
재귀함수는 함수 안에 지 함수가 들어가는 걸 말한다.

즉, 나누는 건 2//2 = 0 이 나오므로 최고 마지막값이니까 그 것을 인지하고 빠져나올 구멍으로 만들어주는 것!
'''

def DFS(x):
    if x==0:
        return
    else:
        DFS(x//2)
        print(x%2, end='')

if __name__=='__main__':
    n=int(input())
    DFS(n)

print('')
# 답 한번 더 복기하는 과정
def func(x):
    # 몫 산출
    if x==0:
        # 재귀에서 빠져나올 구멍 만들기
        return
    else:
        func(x//2)
        print(x%2)

func(11)



### [06. Dynamic Programming(동적계획법) - 02]  이진트리 순회(깊이우선탐색)
'''
난이도: 상

깊이우선탐색이란?
깊이를 우선으로 쭉 탐색해가는 과정

트리탐색순서
1. 전위순회 : 항상 왼쪽. 없으면 백하고 오른쪽.
2. 중위순회 : 왼쪽, 부모, 오른쪽 순서로 출력
3. 후위순회 : 왼쪽, 오른쪽, 부모 순서로 출력

※ 핵심 ※
자식노드(왼)는 부모노드*2, 자식노드(오)는 부모노드*2+1
''' 


# 풀이과정

# 전위순회
num_list=[1,2,3,4,5,6,7]
num = num_list[-1]

while num > 1:
    if num % 2 == 1:
        print(num, end=' ')
        num -= 1
    else:
        print(num, end=' ')
            num == (num//2)
print(num)



# 답안
def DFS(v):
    if v > 7:
        return
    else:
        # print 가 이쪽(자기 업무를 수행한 뒤 재귀함수) 이면 전위순회방식
        print(v, end=' ')
        DFS(v*2)
        # print 가 이쪽이면 중위순회
        # print(v, end=' ')
        DFS(v*2+1)
        # print 가 이쪽이면 후위순회
        # print(v, end=' ')
DFS(1)



### [06. Dynamic Programming(동적계획법) - 03]  부분집합 구하기(DFS)

# 풀이과정
n=3
# n+1개만큼의 0리스트 생성
ch=[0,0,0,0]

def DFS(x):
    if x>n:
        for i in range(1, n+1):
            if ch[i]==1:
                print(i, end=' ')
    else:
        ch[x] = 1
        DFS(x+1)
        ch[x] = 0
        DFS(x+1)

DFS(1)


# 답안
def DFS(x):
    if x==n+1:
        for i in range(1,n+1):
            if ch[i]==1:
                print(i, end=' ')
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)
    
if __name__ == '__main__':
    n=int(input())
    ch=[0]*(n+1)
    DFS(1)
