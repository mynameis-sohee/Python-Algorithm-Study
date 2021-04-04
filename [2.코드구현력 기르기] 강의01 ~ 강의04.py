### [02.코드 구현력 기르기 - 01] K번째 약수

# 풀이 과정 -> 성능측정결과 답안이 더 빠름
def number(num,ind):
    alist=[]
    for i in range(1,num+1):
        if num%i == 0 :
            alist.append(i)
    try: print(alist[ind-1])
    except IndexError: print(-1)
a, b = map(int, input().split())
number(a,b)


# 답안
def answer(n,k):
    cnt=0
    for i in range(1,n+1):
        if n%i==0:
            cnt+=1
        if cnt==k:
            print(i)
            break
    else:
        print(-1) #break 등으로 끊기지 않고 끝까지 수행되었을 경우 else문 출력

a, b = map(int, input().split())
answer(a,b)




### [02.코드 구현력 기르기 - 02] K번째 수
import random as r

# 풀이 과정 -> 성능측정결과 내 풀이코드가 더 빠름
T = int(input())
for i in range(0,T):
    N, s, e, k = map(int, input().split())
    prob = list(map(int, input().split()))
    prob_=prob[s-1:e]
    prob_.sort()
    print('#{}'.format(i+1), prob_[k-1]) 

# 답안
start_time = time.time()
T = int(input())
for t in range(T):
    n,s,e,k=map(int,input().split())
    a=list(map(int,input().split()))
    a=a[s-1:e]
    a.sort()
    print('#%d %d' %(t, a[k-1]))



### [02.코드 구현력 기르기 - 03] K번째 큰 수

import random as r

def big_num(N,K,cards):
    res = set() #set: (1) 중복허용 않고 (2) 순서없는 {}(집합자료형)
    for i in range(N):
        for j in range(i+1,N):
            for q in range(j+1,N):
                res.add(cards[i]+cards[j]+cards[q])
    res=list(res)
    res.sort(reverse=True)
    return res[K-1]

N,K=map(int, input().split())
cards = list(map(int, input().split()))
print(big_num(N,K,cards))



### [02.코드 구현력 기르기 - 04] 선수지식 - 최솟값 구하기

import time
arr = [5,3,7,9,6]

# 풀이 과정 -> 성능측정결과 내 풀이코드가 더 빠름
arr.sort()
print(arr[0])

# 답안
arrmin=arr[0]
for i in range(1, len(arr)):
    if arr[i]<arrmin:
        arrmin=arr[i]
print(arrmin)


