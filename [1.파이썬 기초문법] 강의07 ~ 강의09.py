### [01.파이썬 기초문법 - 07] 문자열과 내장함수

msg = "Hello "
print(msg.upper()) # 출력결과: HELLO 
print(msg.lower()) # 출력결과: hello
print(msg.find('l')) # 출력결과: 2 (첫번째 인덱스 출력)
print(msg.count('l')) # 출력결과: 2
print(msg[:2]) # 출력결과: He (인덱스 0부터 인덱스 1 출력)

for i in range(len(msg)):
    print(msg[i], end=' ') # 출력결과: H e l l o
print()
for i in msg:
    print(i, end=' ') # 출력결과: H e l l o
print()
for i in msg:
    if i.isupper():
            print(i, end=' ') # 출력결과: H (이유: isupper는 대문자이면 참을 return, 반대: islower)
print()
for i in msg:
    if i.isalpha():
            print(i, end=' ') # 출력결과: H e l l o (이유: 알파벳이면(=공백이 아니면) 출력)
print()

# 아스키코드(ASCII): 숫자로 문자를 표현하기 위한 일종의 약속. 특수문자, 숫자, 문자 등에 번호를 부여해 컴퓨터 처리를 쉽게 만든 것
tmp='AZ'
for i in tmp:
    print(ord(i)) # 출력결과: 65 \n 90 (이유: 아스키넘버 출력)

tmp='az'
for i in tmp:
    print(ord(i)) # 출력결과: 97 \n 122 (이유: 아스키넘버 출력)

tmp=65
print(chr(tmp)) # 출력결과: A (이유: 아스키넘버에 해당하는 알파벳 출력)




### [01.파이썬 기초문법 - 08] 리스트와 내장함수 (1)

a=[]
b=list(range(1,11))
b.insert(3,7) # 3번 인덱스에 7 삽입
print(a,b) # 출력결과: [] [1, 2, 3, 7, 4, 5, 6, 7, 8, 9, 10]

b.pop()
print(b) # 출력결과: [1, 2, 3, 7, 4, 5, 6, 7, 8, 9] (이유: 맨 뒤에자리 값 빠짐)
b.pop(3)
print(b) # 출력결과: [1, 2, 3, 4, 5, 6, 7, 8, 9] (이유: 특정 인덱스 값 빠짐(3번 인덱스))
b.remove(9)
print(b) # 출력결과: [1, 2, 3, 4, 5, 6, 7, 8] (이유: 특정 값 빠짐(9라는 숫자 찾아서 뺌))

print(b.index(5)) # 출력결과: 4 (이유: 5라는 값은 4번 인덱스에 위치)
print(sum(b)) # 출력결과: 36
print(max(b)) # 출력결과: 8
print(min(b)) # 출력결과: 1

import random as r
r.shuffle(b)
print(b) # 출력결과: [3, 5, 7, 8, 1, 6, 2, 4] (이유: 랜덤 배치)
b.sort()
print(b) # 출력결과: [1, 2, 3, 4, 5, 6, 7, 8] (이유: 오름차순 정렬)
b.sort(reverse=True)
print(b) # 출력결과: [8, 7, 6, 5, 4, 3, 2, 1] (이유: 내림차순 정렬)




### [01.파이썬 기초문법 - 09] 리스트와 내장함수 (2)

a=[23, 12, 35, 53, 11]
for i in range(len(a)):
    print(a[i], end= ' ') # 출력결과: 23 12 35 53 11
for i in a: 
    print(i, end= ' ') # 출력결과: 23 12 35 53 11 (* 위와 아래 명령값 동일)
print()

for i in enumerate(a): 
    print(i, end= ' ') # 출력결과: (0, 23) (1, 12) (2, 35) (3, 53) (4, 11)  (이유: 튜플의 자료구조 형태로, (인덱스번호, 값) 으로 대입되어 출력)
print()

b = (1,2,3,4,5)
print(b[0]) # 출력결과: 1 (주의사항: 튜플은 값의 append, 값수정 불가)

for i in enumerate(a): 
    print(i[0], i[1], end= ', ') # 출력결과: 0 23, 1 12, 2 35, 3 53, 4 11,
print()
for index, value in enumerate(a):
    print(index,value, end=', ') # 출력결과: 위와 동일
print()

if all(50>x for x in a):
    print('Yes')
else: print ('No') # 출력결과: No (이유: 조건에 '모두'참이어야만 True)

if any(50>x for x in a):
    print('Yes')
else: print ('No') # 출력결과: Yes (이유: 한 가지라도 참이면 True)
