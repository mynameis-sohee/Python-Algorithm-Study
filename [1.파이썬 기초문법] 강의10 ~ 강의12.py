### [01.파이썬 기초문법 - 10] 2차원 리스트 생성과 접근

a=[0]*3
print(a) # 출력결과: [0, 0, 0]

a=[[0]*3]
print(a) # 출력결과: [[0, 0, 0]] (이유: 2차원 리스트 생성)
a[0][1] = 1
print(a) # 출력결과: [[0, 1, 0]] (이유: a의 0행1열을 1로 변경)

a=[[0]*3 for _ in range(3)] # 변수없이 3번 반복. [0]*3 행위를 3번 진행
print(a)
for i in a: # n번째 행 출력 : 형태 [0, 0, 0]
    for n in i: # n번째 열(값) 출력 : 형태 0
        print(n, end=' ')
    print() # 출력결과: 0 0 0 *3열 (리스트의 값만 출력하는 방법)


    
### [01.파이썬 기초문법 - 11] 함수 만들기

def isPrime(x):
    for i in range(2, x):
        if x%i==0: # 나눈 값의 나머지
            return False # return 되면 더이상 함수 실행하지 않고 종료
    return True

a=[12, 13, 7, 9, 19]
for i in a:
    if isPrime(i):
        print(i, end=' ') # 출력결과: 13 7 19 (이유: a 리스트 중 소수인 것들만 출력)


        
### [01.파이썬 기초문법 - 12] 람다함수

plus_two = lambda x: x+2
print(plus_two(1))

a=[1,2,3]
print(list(map(plus_two, a))) # 출력결과: [3,4,5] (이유: map은 리스트 요소를 지정된 함수로 처리해주는 함수, list(map(함수, 리스트)))
print(list(map(lambda x: x+1, a))) # 출력결과: [2,3,4]
