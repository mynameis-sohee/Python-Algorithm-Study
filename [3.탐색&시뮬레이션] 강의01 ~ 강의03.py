### [03.탐색&시뮬레이션 - 01] 회문 문자열 검사

# 풀이과정 - 내 풀이과정은 '전체를 한 번에 출력하도록' 설계. 방법론은 동일
N = int(input())
answer = []

for i in range(0,N):
    word = input().upper()
    if word == word[::-1]:
        answer.append('YES')
    else: answer.append('No')

for i in range(0, len(answer)):
    print('#{}'.format(i+1), answer[i])

    
# 답안 - 답안은 '한 줄씩 출력하도록' 설계
n=int(input())
for i in range(n):
    s=input()
    s=s.upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))



### [03.탐색&시뮬레이션 - 02] 숫자만 추출

# 풀이과정 - str값을 리스트에 넣고 숫자화하여 더하는 과정으로 풀이
input_value = input()
num_list = []

for i in input_value:
    try: int(i)
    except ValueError: continue
    num_list.append(i)
print(int(''.join(num_list)))


# 답안 - for문 안에서 자릿수를 10씩 곱해 출력 (중요)
# i.isdecimal(): 해당 숫자 i가 0~9 사이에 위치하면 True, 그렇지 않으면 False 출력하는 내장함ㅎ수
input_value = input()
answer = 0

for i in input_value:
    if i.isdecimal():
        answer = answer*10 + int(i)
    else: continue
print(answer)


## [03.탐색&시뮬레이션 - 03] 카드 역배치

# 풀이과정
list_ = list(range(1, 21))

for i in range(10):
    small, large = map(int, input().split())
    list_ = list_[:small-1]+list_[small-1:large-1][::-1]+list_[large-1:]
    print(list_)
    
    
 
# 답안
a = list(range(21))
for _ in range(10):
    s, e = map(int, input().split())
    for i in ragne((e-s+1)//2):
        a[s+i], a[e-i]=a[e-i], a[s+i]
# 생성된 0번째 index값 삭제(0번째 index값:0, pop(삭제하고 싶은 index값, 공백 시 맨 마지막 index값 삭제)
a.pop(0)
for x in a:
    print(x, end=' ')
