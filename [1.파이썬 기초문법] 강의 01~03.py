### [01.파이썬 기초문법 - 01] print
a, b, c = 1,2,3

print(a,b,c) # 출력결과: 1 2 3
print(a,b,c, sep=', ') # 출력결과: 1, 2, 3

print(a) # 출력결과: 1이고, sep='\n'
print(a, end=' ')
print(b) # 출력결과: 1 2 (이유: end=' ')



### [01.파이썬 기초문법 - 02] 변수입력과 연산자
a = input('숫자를 입력하세요 :')
print(a) #출력결과: input에 넣은 값

a, b = input('숫자를 입력하세요 :').split() # 띄어쓰기 기준으로 분리
print(a+b) #출력결과: 'a'+'b' (이유: str로 받기 때문)

a, b = map(int, input('숫자를 입력하세요 :').split())
print(a+b) # 출력결과: a+b
print(a//b) # 출력결과: a/b의 몫
print(a%b) # 출력결과: a/b의 나머지
print(a**b) # 출력결과: a의 b제곱

a, b = 0.5, 3 
c = a+b
print(type(c)) # 출력결과:float (이유: 형이 다른 것을 연산하면 더 큰 범위로 설정됨 <형변환>)



### [01.파이썬 기초문법 - 03] 조건문
x = 17
if x >= 10:
    if x%2 == 1: print('10 이상의 홀수') # 중첩if문

x = 9
if x>0 and x<10: print('10보다 작은 자연수') # and 연산으로 중첩if문
if 0<x<10: print('10보다 작은 자연수') # 상기 결과값과 동일

if x<3: print('A')
elif x<5: print('B')
else: print('C') # 다중if문
