### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 09] 증가수열 만들기(그리디)
'''
특이사항: 내 풀이과정은 단순 일반 증가수열. 최적 증가수열이 아니므로 정답이 아님. 다시 풀어보아야 함!
'''

# 풀이과정 - 정답 X
n = int(input())
num_list = list(map(int, input().split()))

answer = 0
ans_slist = []

from collections import deque
num_list = deque(num_list)

max_num = 0
while max_num < max(num_list):
    if ((num_list[-1]) <= (num_list[0])):
        if max_num <= num_list[-1]:
            ans_slist.append('R')
            max_num = (num_list.pop())
        else:
            ans_slist.append('L')
            max_num = (num_list.popleft())
    elif (num_list[-1]) > (num_list[0]):
        if max_num <= num_list[0]:
            ans_slist.append('L')
            max_num = (num_list.popleft())
        else:
            ans_slist.append('R')
            max_num = (num_list.pop())
print(ans_slist)



### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 10] 역수열 만들기(그리디)
'''
특이사항: 문제 해결X
'''
# 답안
n=int(input())
a=list(map(int, input().split()))
a.insert(0,0)
seq=[0]*n
for i in range(1,n+1):
    for j in range(n):
        if a[i]==0 and seq[j]==0:
            seq[j]=i
            break
        elif seq[j]==0:
            a[i]-=1
for x in seq:
    print(x, end=' ')
