### [03.탐색&시뮬레이션 - 04] 두 리스트 합치기

# 풀이과정 - 해당 방법은 리스트의 개수가 8개니까 8log8번 진행해야 sort가 된다. 따라서 최적으로 하려면 하나씩 비교하는 방법이 좋고, 이는 답안에 있다. 이는 n번만 비교해주면 된다.

N, M = int(input().split())
list_ = []

for _ in range(2):
    _list_ = list(map(int, input().split()))
    list_.extend(_list_)

list_.sort()
for i in list_:
    print(i, end=' ')


    
# 답안
a = list(map(int, input().split()))
b = list(map(int, input().split()))
m, n = int(input().split())
p1 = p2 = 0
c = []

while p1<n and p2<m:
    if a[p1]<=b[p2]:
        c.append(append[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
print(c)



### [03.탐색&시뮬레이션 - 05] 수들의 합

# 풀이과정
N, M = map(int, input().split())
_list_ = list(map(int, input().split()))
cnt = 0
lt = 0
rt = 1

while lt < N:
    if lt == rt :
        rt += 1
    if sum(_list_[lt:rt]) == M:
        cnt += 1
        lt += 1
    if sum(_list_[lt:rt]) > M:
        lt += 1
    if sum(_list_[lt:rt]) < M:
        rt += 1
        # 마지막 인덱스값만 남았을 때, 무한 Loop를 돌 수 있으므로 반드시 지정
        if lt == N-1:
            lt += 1
print(cnt)



# 답안
n, m = map(int, input().split()))
a = list(map(int, input().split()))
lt = 0
rt = 1
# tot: 연속 부분의 합
tot = a[0]
cnt = 0
while True:
    if tot<m:
        if rt<n:
            tot+=a[rt]
            rt+=1
        # m(값)이 이미 남은 인덱스 끝까지의 총합보다 더 작으니까 더 연산할 필요가 없으므로 종료 (중요)
        else: break
    if tot==m:
        cnt+=1
        tot-=a[lt]
        lt+=1
    else:
        tot-=a[lt]
        lt+=1
print(cnt)



### [03.탐색&시뮬레이션 - 06] 격차판 최대합

# 풀이과정 - numpy 사용해 array
import numpy as np

N = int(input())
_list_ = []

for i in range(0, N):
    __list__ = list(map(int, input().split()))
    _list_.append(__list__)
_list_ = np.array(_list_)

cnt = 0
ans = 0
ans_ = 0

for i in range(0, N):
    if _list_[:,i].sum() > cnt:
        cnt = _list_[:,i].sum()
    if _list_[i,:].sum() > cnt:
        cnt = _list_[i,:].sum()

for i in range(0, N):
    ans += _list_[(-1*i)-1,i]
    ans_ += _list_[i,i]

if ans > cnt:
    cnt = ans
if ans_ > cnt:
    cnt = ans_

print(cnt)



# 답안 - 어레이를 만든 뒤, numpy 없이 연산하는 방법: 한 개씩 추출 list[i][j] 하여 sum
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 가장 작은 값으로 초기화
largest = -210349303

# 가로와 세로 각 행렬 합 산출하는 for문
for i in range(n):
    # 행의 합: sum1, 열의 합: sum2
    sum1=sum2=0
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2
sum1 = sum2 = 0

# 대각선 합 구하는 for문
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
    
print(largest)

