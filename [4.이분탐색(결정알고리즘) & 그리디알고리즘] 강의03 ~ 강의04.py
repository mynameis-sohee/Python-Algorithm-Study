
### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 03] 뮤직비디오(결정알고리즘)
'''
문제: N개를 M개로 묶을 건데, N개의 그룹의 최대값과 최소값 간극이 적어야 함
체감난이도: 상
이슈: N개를 M개로 묶는 것 까지 가능하며, 각 그룹의 최대.최소값 간극이 적은 최적해 산출 X
'''

# 풀이과정
N, M = map(int, input().split())
count_list=[map(int, input().split())]

N = 9
M = 3
count_list = [1,2,3,4,5,6,7,8,9]

min_cnt = 1
max_cnt = sum(count_list)
mid_cnt = (min_cnt+max_cnt)//2


while True:
    cnt = 0
    sub_cnt = 0
    for i in count_list:
        if sub_cnt+i <= mid_cnt:
            sub_cnt += i
        else:
            cnt += 1
            sub_cnt = i
    if sub_cnt > 0:
        cnt += 1

    if cnt == M:
        print(mid_cnt)
        break
    elif cnt < M:
        max_cnt = mid_cnt
        mid_cnt = (max_cnt+min_cnt)//2
    elif cnt > M:
        min_cnt = mid_cnt
        mid_cnt = (max_cnt+min_cnt)//2



### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 04] 마구간 정하기(결정알고리즘)
'''
문제: C마리의 말을 각 좌표(=마구간)에 넣는데, 가까운 두 말의 거리가 최대가 될 수 있는 값 출력
체감난이도: 상
재풀이 결과: X (다시 풀어보아야 함)
이슈: 풀이를 보고 이해했으므로, 다시 풀어보아야 함
'''

# 풀이과정(=답안)
N, C = 5, 3
num_list = [1,2,8,4,9]

# 1. num_list sort
num_list.sort()

# Count 함수(len=mid_num, cnt는 C와 값이 같아야 정답)
def Count(len):
    cnt=1
    ep=num_list[0] # 첫번째 마구간에 첫번째 말 배치
    for i in range(1, N):
        if (num_list[i]-ep) >= len:
            cnt+=1
            ep=num_list[i] # 그 다음 말의 위치를 배치
    return cnt

min_num = 1
max_num = num_list[-1]

while min_num<=max_num:
    # mid_num : 가장 가까운 두 말의 거리
    mid_num = (min_num+max_num)//2
    if Count(mid_num)>=C:
        answer = mid_num
        min_num = mid_num+1
    else:
        max_num=mid_num-1
print(answer)
