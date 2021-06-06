
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의06 중복순열 구하기
'''
풀이결과: 정답
'''

# 풀이과정
def DFS(x):
    if x>m:
        for i in range(1,m+1):
            print(res[i], end=' ')
        global cnt
        cnt+=1
        print('')
        return

    else:
        for i in range(1,n+1):
            res[x]=i
            DFS(x+1)


if __name__ == '__main__':
    n, m = map(int, input().split())
    res = [0]*(m+1)
    cnt = 0
    DFS(1)
    print(cnt)




### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의07 동전교환

'''
풀이결과: 정답
포인트: 1개당 n개씩 뻗는 DFS면 for문을 이용하고, sort 를 활용
'''

# 풀이과정
def DFS(x, sum):
    global min_cnt
    if sum > total:
        return
    if sum == total:
        if x < min_cnt:
            min_cnt = x
    else:
        for i in range(n):
            DFS(x+1, sum+cash_list[i])
        
if __name__=='__main__':
    n=3
    cash_list=[1,2,5]
    cash_list.sort(reverse=True)
    total=15
    min_cnt = 129310398
    DFS(0, 0)
    print(min_cnt)


    


### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의08 순열구하기(DFS)

'''
풀이결과: 정답
비복원 순열
'''

# 풀이과정

def DFS(x):
    if x>m:
        if len(set(res)) == m+1:
            for i in range(1, m+1):
                print(res[i], end=' ')
            print('')
            global cnt
            cnt+=1
        return
    else:
        for i in range(1,n+1):

            res[x]=i
            DFS(x+1)
    

if __name__=='__main__':
    n=3
    m=2
    res=[0]*(m+1)
    res[1]=1
    cnt=0
    DFS(1)
    print(cnt)

