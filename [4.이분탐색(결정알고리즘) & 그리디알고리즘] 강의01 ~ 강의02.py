### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 01] 이분 검색

# 풀이과정
n, m = map(int, input().split())
num_list = list(map(int, input().split()))

start_index = 0
end_index = len(num_list)+1

num_list.sort()

while start_index <= end_index:
    mid_index = (start_index + end_index)//2
    if num_list[mid_index] == m:
        print(mid_index+1)
        break
    if num_list[mid_index] < m:
        start_index = mid_index+1
    if num_list[mid_index] > m:
        end_index = mid_index


# 답안
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt=0
rt=n-1

while lt<=rt:
    mid=(lt+rt)//2
    if a[mid]==m:
        print(mid+1)
        break
    elif a[mid]>m:
        rt=mid-1
    else:
        lt=mid+1



### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 02] 랜선 자르기(결정알고리즘)
# 특징: 자를 때, 여분 남은 것은 재사용할 수 없으며 랜선 자를 때 소비되는 랜선은 0이라는 가정 하에 진

k, n = map(int, input().split())
num_list = []

for _ in range(k):
    num = int(input())
    num_list.append(num)

max_num = max(num_list)

while True:
    opt_num = max_num//2
    answer = 0
    for i in num_list:
        answer += i//opt_num
    if answer == n:
        print(opt_num)
        break
    else:
        max_num = opt_num
