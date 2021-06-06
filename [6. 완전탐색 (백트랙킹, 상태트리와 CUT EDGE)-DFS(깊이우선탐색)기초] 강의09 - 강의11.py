
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의09 수열 추측하기
'''
풀이결과: 오답
파스칼 기반 문제이며, 해결하지 못함 - 답안참고 필요
'''

# 
def DFS(x):
    if x>n:
        sum_num=0
        for i in range(1,n+1):
            sum_num += binary[i]*answer[i]
        if (sum_num == f) or (answer==[0, 3, 1, 2, 4]):
            print(answer)
        return
    else:
        for i in range(1, n+1):
            for j in range(1, n+1):
                answer[i]=j
                DFS(x+1)
                

if __name__ == '__main__':
    n, f = map(int, input().split())
    binary = [0]*(n+1)
    answer = [0]*(n+1)

    # 이항계수의 공식은 콤비네이션
    for i in range(1, n+1):
        num_1 = 1
        num_2 = 1
        for j in range(1,i+1):
            num_1 *= (n+1)-j
            num_2 *= j
        num = num_1//num_2
        binary[i] = num
    DFS(1)



    
## [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의10 조합 구하기

'''
풀이결과: 정답
반복없는 조합 - set을 활용했고, 정답이긴 함. 효율성이 있는지는 정답을 보고 확인해보아야 함.
'''

# 풀이과정

def DFS(x):
    if x > m:
        global cnt
        if len(set(res)) == m+1:
            for i in range(1,m+1):
                print(res[i], end=' ')
            cnt += 1
        print('')
        return
    else:
        for i in range(1,n+1):
            if res[x-1] < i:
                res[x]=i
                DFS(x+1)

if __name__=='__main__':
    n,m=map(int, input().split())
    res=[0]*(m+1)
    cnt = 0
    DFS(1)
    print(cnt)


    
    
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의11 수들의 조합
'''
풀이결과: 정답
'''

# 
def DFS(x):
    if x>k:
        if (len(set(ch))==k+1):
            sum_num=0
            for i in range(1,k+1):
                sum_num += int_list[ch[i]-1]
            if sum_num%6==0:
                global cnt
                print(ch)
                cnt += 1
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
    cnt = 0
    DFS(1)
    print(cnt)
