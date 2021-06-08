
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의11 수들의 조합
# 이는 순서가 필요없으므로 이게 가능하다.

'''
풀이결과: 정답
-
중복 리스트의 중복제거방법: 에러 TypeError: unhashable 
type: 'list'

중복리스트는 set이 어렵다. tuple로는 set이 가능하다. 따라서 리스트안에있는 리스트는 순서가 없는(왜냐하면 조합에서는 순서 필요 없으므로) 튜플형태로 저장한다.
그리고 그 튜플리스트에 set을 취한다. 
https://inma.tistory.com/132

-
'''

# 풀이과정

def DFS(x):
    if x>k:
        if (len(set(ch))==k+1):
            sum_num=0
            for i in range(1,k+1):
                sum_num += int_list[ch[i]-1]
            if sum_num%6==0:
                answer_list.append(tuple(set(ch)))

        return
    else:
        for i in range(1,n+1):
            ch[x]=i
            DFS(x+1)

if __name__=='__main__':
    n=5
    k=3
    int_list=[2,4,5,8,12]
    ch=[0]*(k+1)
    answer_list=[]
    DFS(1)
    answer = len(set(answer_list)) 
    print(answer)
    
    

# 라이브러리로 구현하는 방법

import itertools as it

n, k = map(int, input().split())
a=list(map(int, input().split()))
m=int(input())

cnt=0
for x in it.combinations(a, k):
    # print(x)
    if sum(x)%m==0:
        cnt+=1
print(cnt)





### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의12 인접행렬(가중치 방향그래프)
'''
풀이결과: 정답
'''

# 풀이과정
n, m = map(int, input().split())
num_list = []
for i in range(m):
    num = list(map(int, input().split()))
    num_list.append(num)

for i in range(1,n+1):
    answer=[0]*n
    for j in range(m):
        if num_list[j][0]==i:
            answer[num_list[j][1]-1]=num_list[j][2]
    print(answer)


