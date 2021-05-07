# [03.탐색&시뮬레이션 - 08] 곶감(모래시계)

# 풀이과정
'''
  핵심개념: pop()
  리마인드 포인트: array값을 변동하고 합해야 하는 경우, array 변동요인을 모두 적용해준 뒤 합하자.
                   이때, array의 리스트를 끌어 와 합치는 것이 아닌, 개별 요소로 뽑아 합쳐준다. 
'''

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s = 0 
e = n
m = int(input())

# 1. array 값 변동부분 수정
for i in range(m):
    h, j, k = map(int, input().split())
    if j == 0 :
        for _ in range(k):
            # 값을 빼내고 뒤로 append 하는 것이 한 번에 실행, pop문은 출력된 값으로 return (중요)
            a[h-1].append(a[h-1].pop(0))
    else: 
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())

            
# 2. 모래시계 형태로 array 합하기
for i in range(0, n):
    for j in range(s, e):
        res+=a[i][j]

    if i < n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1

print(res)



### [03.탐색&시뮬레이션 - 09] 봉우리

# 풀이과정 -  맞지만 dx, dy 활용 시 반복되는 작업 정의 수정 필요
'''
  핵심개념: array의 상하좌우 값 탐색 시 dx, dy 리스트 활용
'''

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    a[i].insert(0, 0)
    a[i].insert(n+1, 0)
a.insert(0, list(0 for _ in range(n+2)))
a.insert(n+1, list(0 for _ in range(n+2)))

cnt = 0
for i in range(1, n+1):
    for j in range(1, n+1):
        if (a[i][j] > a[i+dx[0]][j+dy[0]]) and  (a[i][j] > a[i+dx[1]][j+dy[1]]) and  (a[i][j] > a[i+dx[2]][j+dy[2]]) and  (a[i][j] > a[i+dx[3]][j+dy[3]]):
            cnt += 1
print(cnt)


# 답안
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n=int(input())
a=[list(map(int, input().split())) for _ in range(n)]

# 0을 n개만큼 생성한 리스트를 각각 0번째, 마지막에 넣는다는 의미
a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)
cnt=0

# 해당 조건을 모두 만족(all)하면 cnt에 1을 추가하라는 의미 (중요)
for i in range(1, n+1):
    for j in ragne(1, n+1):
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

            

## [03.탐색&시뮬레이션 - 10] 스도쿠 검사
# 풀이과정 - 가로.세로 중복 여부 확인 알고리즘 성공했으나, array(집합) 내 중복 여부 확인 알고리즘 실패

'''
  핵심개념: array 값 내 중복이 있는지 & 특정 숫자범위내에 해당하는지 검사할 때, 0 리스트를 활용하는 방법 (중요)
'''

a = [list(map(int, input().split())) for _ in range(9)]

# 조건1. 각행에 1부터 9까지 숫자가 중복없어야함

for i in range(9):
    if len[set(a[i])] == 9 :
        for j in range(9):
            if a[i][j] <= 9 and a[i][j] >= 0:
                continue
            else: break
    else: break

# 열 리스트 만들기
list_=[]
for i in range(9):
    for j in range(9):
        list_ = list_.append(list_[i][j])
    if len[set(list_)] == 9 :
        for k in range(9):
            if list_[k] <= 9 and list_[k] >= 0:
                continue
            else: break

# 어레이 리스트 만들기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


#답안

def check(a):
    for i in range(9):
        ch1=[0]*10
        ch2=[0]*10
        for j in range(9):
            ch1[a[i][j]]=1
            ch2[a[j][i]]=1
        if sum(ch1)!=9 or sum(ch2)!=9:
            return False
    
    for i in range(3):
        for j in range(3):
            ch3=[0]*10
            for k in range(3):
                for s in range(3):
                    ch3[a[i*3+k][j*3+s]]=1
            if sum(ch3)!=9:
                return False
    return True

a = [list(map(int, input().split())) for _ in range(9)]

if check(a): 
    print("YES")
else: 
    print("NO")

    
    

## [03.탐색&시뮬레이션 - 11] 격자판 회문수

# 풀이과정 - 행 회문수의 경우 성공했으나 열 회문수 산출 실패(시도하고자 하는 방법론은 맞았으나 코드 구현 실패했으므로 다시 도전 필요)
'''
  핵심개념: 격자판 열값 회문수 확인 방법 (중요)
'''

a = [list(map(int, input().split())) for _ in range(7)]
s = 0
n = 5
cnt = 0

# 격자판 행값 확인
for i in range(7):
    for j in range(0,3):
        if a[i][j:j+5] == a[i][j:j+5][::-1]:
            cnt+=1
# 격자판 열값 확인
for j in range(7):
    for i in range(3):
        if a[s][j] == a[n][j]:
            s+=1
            n-=1


# 답안
a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

for i in range(3):
    for j in range(7):
        # 격자판 행값 확인
        tmp=board[j][i:i+5]
        if tmp==tmp[::-1]:
            cnt+=1
        # 격자판 열값 확인 (중요)
        # 5//2 = 2 이므로, 몫 값인 2만큼 for
        for k in range(2):
            if board[i+k][j]!=board[i+5-k-1][j]
                break
        else:
            cnt+=1
print(cnt)
