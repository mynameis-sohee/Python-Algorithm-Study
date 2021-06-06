### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초 03 ] 강의03 부분집합 구하기
## 2021.06.06 복습
'''
풀이결과: 정답
'''

# 풀이과정
def DFS(x):
    if x>n:
        for i in range(n+1):
            if ch[i]==1:
                print(i, end=' ')
        print('')
        return
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)



if __name__ == '__main__':
    n = int(input())
    ch = [0]*(n+1)
    DFS(1)



    
    
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의04 합이 같은 부분집합
## 2021.06.06 복습
'''
풀이결과: 정답
'''

# 풀이과정
import sys

def DFS(x):
    
    if x>n:
        sum_num = 0
        for i in range(n+1):
            if ch[i] == 1:
                sum_num += num_list[i-1]
        if sum_num == sum(num_list)/2:
            print('YES')
            sys.exit()
    else:
        ch[x]=1
        DFS(x+1)
        ch[x]=0
        DFS(x+1)

if __name__ == '__main__':
    n = int(input())
    ch = [0]*(n+1)
    num_list=[1,3,5,6,7,10]
    DFS(1)

    # 이건 DFS(1)에서 exit이 되지 않으면 출력될 것이다. exit은 아예 시스템에서 빠져나간다는 뜻이므로.
    print('NO')
    
    
    
    

    
### [6. 완전탐색 (백트랙킹, 상태트리와 CUT EDGE)-DFS(깊이우선탐색)기초] 강의05 바둑이 승차(DFS)
'''
풀이결과: 정답
'''

# 풀이과정
def DFS(x):
    global max_kg
    if x>n:
        cnt_kg = 0
        for i in range(n+1):
            if ch[i]==1:
                cnt_kg += num_list[i-1]
        if cnt_kg <= C and cnt_kg>max_kg:
            max_kg = cnt_kg
            max_list.append(max_kg)
        return

    else:
        ch[x]=1
        DFS(x+1)

        ch[x]=0
        DFS(x+1)

        
if __name__ == '__main__':
    C, n=map(int, input().split())
    ch=[0]*(n+1)
    max_kg = -123124
    max_list = []
    num_list=[81,58,42,33,61]
    DFS(1)
    print(max_list.pop())


    if x>n:
        for i in range(n+1):
            for j in range(n+1):
                if ch_1[i] == 1 and ch_2[j] ==1:
                    print(i, j)
        return



