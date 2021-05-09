### [05. 자료구조(스택, 큐, 해쉬, 힙) - 08] 단어찾기(해쉬)

'''
문제풀이 핵심: 딕셔너리를 사용하자.

--- 딕셔너리 특징 ---
1. 단어도 키값으로 정할 수 있다.
2. KEY, VAL 순서로 딕셔너리 아이템에 접근할 수 있다. (dict.items() 를 이용)
4. 그리고 한 개의 dict에는 똑같은 key는 존재하지 않는다.
'''

'''
해쉬테이블 사용방법: 순서가 의미없고, 이미 알고 있는 정보로 저장된 정보를 검색하는 방법에 적용

-Direct Access Table-
인덱스배열: O(1) 방법
설명: Index를 Key로 인식하고 Data에 접근하는 방법
장점: 직관적이고 효율적이다
단점: Key 범위가 커짐에 따라, 차지하는 공간이 많아진다. 이는 불필요한 공간낭비를 야기할 수 있다.

-Hash Table-
해쉬배열
설명: 해쉬함수를 통해, Key를 원하는 범위의 특정 자연수로 반환. 이 값을 Key(Index)로 사용하는 Table
특징: 원래 Key값, Value를 특정 해시 한 값에 저장

    특정값 범위 Hash함수 방법
    1. 나누기
        - 배열크기가 200이면, 200으로 나눠 남은 나머지로 값을 저장
    2. 곱하기
        - 0<a<1인 값과 Key 값을 곱해 나온 값의 소수점을 배열크기와 곱해 해쉬값 생성
'''


# 풀이과정
using_word = ['big', 'good', 'sky', 'blue', 'mouse']
used_word = ['sky', 'good', 'mouse', 'big']

answer = dict()
for i in using_word:
    answer[i] = 0

for i in used_word:
    answer[i] = 1


for key, val in answer.items():
    if val == 0:
        print(key)
        break



### [05. 자료구조(스택, 큐, 해쉬, 힙) - 09]  아나그램 : 구글 인터뷰 문제
'''
--- 문제 풀이 포인트 ---
1. 기준값을 +1하여 딕셔너리 생성
2. 비교값을 -1하여 딕셔너리 생성

문제풀이 핵심: get
'''


# 풀이과정
test = 'AbaAeCe'
samp = 'baeeACA'

answer = dict()

for i in test:
    # 만약 i라는 값이 answer key에 존재한다면 if문을 돌리도록 만드는 과정
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for k in samp:
    if k in answer:
        answer[k] -= 1
    else:
        # 여기서 더 효율적으로 바꾸는 방법 -> 답안 참고
        answer[k] = -1
        break

# 이렇게하면 굳이 필요하지 않은 key도 저장해야 하니까 용량이 부족해지므로, 아래 답안을 참고하기
for key, val in answer.items():
    if val != 0:
        print('NO')
        break
else:
    print('YES')



# 답안
a = 'AbaAeCe'
b = 'baeeACA'

answer = {'A':1}

for x in a:
    # 딕셔너리 안에 찾으려는 Key 값이 없을 경우 미리 정해 둔 디폴트 값을 대신 가져오게 하고 싶을 때에는 get(x, '디폴트 값')을 사용. 만약 key값이 존재하면 특정 key에 할당된 val 값이 출력
    answer[x]=answer.get(x, 0)+1
for x in b:
    answer[x]=answer.get(x, 0)-1
for x in a:
    # get을 사용하면 key(x)값의 val이 출력됨
    if answer.get(x) != 0:
        print('NO')
        break
else:
    print('YES')

    
    
### [05. 자료구조(스택, 큐, 해쉬, 힙) - 10]  최소힙(힙)
'''
--- 힙 설명 ---

개념: 2개의 조건을 만족하는 트리

특징: 노드 개수가 n이면, 높이(Lev)는 O(log(n))
    조건1) 형태속성 - ※ 완전이진트리여야 한다.
    조건2) 힙속성 - 트리 내 모든 노드의 데이터는 자식 노드들의 데이터보다 크거나 같다. (최소힙은 반대)
  ※ 완전이진트리 기준: (1) 마지막 Lev제외 나머지 모두 이진  (2) 마지막 Lev의 경우, 왼쪽에서 오른쪽으로 채워진 형태

heap 핸들링 방법: heappush, heappop


문제풀이 핵심: 노드의 위부터 한 개씩 넣고, n번째 레벨에 수를 넣기 전, 부모노드보다 작은지 확인. 만약 부모노드가 더 작으면, 부모노드와 위치 변경(최대힙 기준)
'''


# 답안
import heapq as hq

a=[]
int_list=[5,3,6,0,5,0,2,4,0,-1]

while True:
    n=int(1)
    if n == -1:
        break
    if n == 0:
        # 힙 자료구조에 데이터가 없는 경우
        if len(a) == 0:
            print(-1)
        else:
            # a에서 자료를 하나 빼줌과 동시에 출력된다는 의미
            print(hq.heappop(a))
    else:
        # a라는 리스트에 n값을 넣으라는 의미
        hq.heappush(a, n)





## [05. 자료구조(스택, 큐, 해쉬, 힙) - 11]  최대힙(힙)
'''
난이도: 상
※ 다시 풀어보기
'''
