### [03.탐색&시뮬레이션 - 07] 사과나무(다이아몬드)

# 풀이과정 - 문제 풀이 X. 십자가로만 더했고, 대각선은 합치지 못함

N = int(input())
_list_ = [list(map(int, input().split())) for _ in range(N)]

right = (N//2)+1
left = N//2

sum_val = 0

for i in range(N//2):
    sum_val += sum(_list_[i][left:right])
    left += -1
    right += 1

right = N
left = 1

for i in range((N//2)+1,N):
    sum_val += sum(_list_[i][left:right])
    left += 1
    right += -1

print(sum_val)



# 답안
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0

for i in range(n):
    for j in range(s, e+1):
        res+=a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
        
        
 
