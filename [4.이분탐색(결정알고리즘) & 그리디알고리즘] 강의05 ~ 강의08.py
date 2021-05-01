

### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 05] 회의실 배정(그리디)
'''
정답 맞췄음 (아이디어는 강의 앞 참고)

그리디 알고리즘 특징
1. 튜플 리스트 생성해서 풀이
2. 최소~최대문제 -> 그리디인지 확인
3. 정렬(sort) 이용해 풀이 or 이슈쉐어링 방법으로 
'''

# 풀이과정
n = int(input())
tuple_list = []

# 튜플 리스트 생성
for k in range(n):
    tup_num = tuple(map(int, input().split()))
    tuple_list.append(tup_num)

# sort의 key: sort 기준값
tuple_list.sort(key=lambda x:x[1])

# 첫번째 회의는 잡아줄 것이므로 1로 시작
cnt = 1
least_time = tuple_list[0][1]

for i in range(1, len(tuple_list)):
    if tuple_list[i][0] - least_time >= 0 :
        least_time = tuple_list[i][1]
        cnt += 1
print(cnt)




### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 06] 씨름선수(그리디)

# 풀이과정
n = int(input())
tuple_list = []

for i in range(n):
    tuple_num = tuple(map(int, input().split()))
    tuple_list.append(tuple_num)

cnt = 0
for i in tuple_list:
    test_hg = i[0]
    test_wg = i[1]

    for k in tuple_list:
        if test_hg < k[0] and  test_wg < k[1]:
            break
    else:
        cnt += 1

print(cnt)



# 답안 -> 왜이렇게 풀었는지 확인해보기
n = int(input())
body = []

for i in range(n):
    a, b = map(int, input().split())
    body.append((a,b))
body.sort(reverse=True)
largest=0
cnt=0
for x, y in body:
    if y > largest:
        largest = y
        cnt += 1
print(c) 




### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 07] 창고 정리(그리디)
'''
중요 아이디어: sort를 활용해 크기별로 나열 후 문제 풀이 (답안 확인)
※ max와 min을 각각 찾아서 풀이하는 방법과 Sort 활용 중, 어떤 것이 효율적일지 확인해보기
'''

# 풀이과정
l = 10

# l개마다 쌓인 박스의 개수
box_list = [6, 42, 68, 76, 40, 87, 14, 65, 76, 81]

# 높이 조정(반복) 횟수
k = 50

for i in range(k):
    min_idx = box_list.index(min(box_list))
    max_idx = box_list.index(max(box_list))
    
    box_list[min_idx] += 1
    box_list[max_idx] -= 1

print(max(box_list)-min(box_list))


# 답안
k = 50

for _ in range(k):
    box_list.sort()

    box_list[0]+=1
    box_list[-1]-=1

box_list.sort()
print(box_list[0])




### [04. 이분탐색(결정알고리즘) & 그리디알고리즘 - 08] 침몰하는 타이타닉(그리디)
'''
이슈: 문제 해결 X
중요 아이디어 - 2개 숫자를 합해서 최적해를 산출하려면, 순차적으로 합하는 것이 아닌 앞뒤로 값을 합해야 한다.
'''

'''
데크(deque)란?
양방향 큐, 즉 앞과 뒤 양 쪽에서 엘리먼트를 추가하거나 제거할 수 있는 것이 데크다.
양 끝 엘리먼트에 대한 append, pop이 빠르다는 장점이 있다.
삽입 제거 시, 일반적인 리스트는 연산에 O(n)인 데에 반해, 데크는 O(1)로 성능이 매우 빠르다.

# 리스트로도 되기는 하는데 리스트는 pop을 하면 모든 값들이 앞으로 당겨지는 현상이 발생. 
# 데크는 앞에서도 뺐다넣다 뒤에서도 뺐다넣다 할수있고 중간자료는 움직이지 않고 빠졌으면 그냥 0이 그다음자료를 의미하는 자료임. 땡기는 연산을 안함

'''

# 풀이과정 - 정답X
n, m = map(int, input().split())
wg_list = list(map(int, input().split()))

wg_list.sort()
# max cnt
cnt=0
idx_sum = 0
idx_cnt = 0

for i in range(len(wg_list)):
    if (wg_list[i]+idx_sum <= m) and (idx_cnt < 2):
        idx_sum += wg_list[i]
    else:
        idx_sum = wg_list[i]
        idx_cnt = 1
        cnt += 1

if idx_sum != 0:
    cnt += 1
print(cnt)


# 답안
n, limit = map(int, input().split())
p = list(map(int, input().split()))
p.sort()


from collections import deque
p = deque(p)

cnt = 0

while p:
    # 한명 나는 조건을 작성
    if len(p) == 1:
        cnt += 1
        break
    # 가벼운 사람과 무거운사람 더했는데 크면 무거운사람만 타고 가서 없어지므로 pop, cnt += 1 
    if p[0]+p[-1] > limit:
        p.pop()
        cnt += 1
    # 제한에 안걸렸으므로 둘이 같이 타고가야한다. 이때 p.pop(0) 하면 맨앞자리다. 앞자리랑 뒷자리 뺀다. 그리고 더해준다.
    else:
        p.popleft() # p.pop(0) 보다 효율적 코드
        p.pop()
        cnt += 1
print(cnt)
