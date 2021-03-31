### [01.파이썬 기초문법 - 04] 반복문(for, while)

for i in range(10, 0, -1): # 1씩 작아지도록 명령
    print(i) #10부터 1까지 순차적으로 print

i=1
while i<=10: # 출력결과: 1부터 10까지 순차적으로 print
    print(i)
    i+=1

i=10
while i>=1: #출력결과: 10부터 1까지 순차적으로 print
    print(i)
    i-=1

while True: 
    print(i)
    if i == 5: 
        break
    i+=1 # 출력결과: 1부터 5까지 순차적으로 print

for i in range(1,11):
    if i%2==0:
        print(i)
    else: continue  # 출력결과: 2,4,6,8,10이 순차적으로 print


for i in range(1,11):
    print(i)
    if i == 5:
        break
else: print(11) # 출력결과: 1부터 10까지 순차적으로 print (이유: for else문은 인위적으로(break) for문이 모두 실행이 안된다면 출력이 안됨)


for i in range(1,11):
    print(i)
    if i == 15:
        break
else: print(11) # 출력결과: 1부터 11까지 순차적으로 print (이유: for else문의 else문은, for문이 정상적으로 종료가 되면 출력됨)



### [01.파이썬 기초문법 - 05] 반복문 이용한 문제풀이

# (1) 1부터 N까지 홀수 출력하기
n=int(input())
for i in range(1, n+1):
    if i%2 ==1 :
        print(i)

# (2) 1부터 N까지 합 출력하기
n=int(input())
sum_number = 0
for i in range(1,n+1):
    sum_number = sum_number + i 
print(sum_number)

# (3) N 약수 출력하기
n=int(input())
for i in range(1,n+1):
    if n%i==0:
        print(i, end=' ') # 출력결과: 1 3 5 15



### [01.파이썬 기초문법 - 06] 중첩반복문

for i in range(5):
    for j in range(i+1):
        print("*",end= ' ')
    print() # 출력결과: * \n * * \n ... 해서 *5개까지 출력. print()때문에 줄바꿈 진행

for i in range(5):
    for j in range(5-i):
        print("*",end= ' ')
    print() # 출력결과: * * * * * \n * * * * \n ... 해서 *1개까지 출력. print()때문에 줄바꿈 진행
