### [02.코드 구현력 기르기 - 05] 대표값

# 풀이과정
def number(N, math_li):
    avg_num = sum(math_li)/N
    min_num = math_li[0]
    min_dev = abs(avg_num-math_li[0])

    for i in math_li:
        abs_dev = abs(avg_num-i)
        if abs_dev < min_dev: 
            min_num = i
            min_dev = abs_dev
    print(min_num, math_li.index(min_num)+1)

N = int(input())
math_li = list(map(int, input().split()))
number(N, math_li)



### [02.코드 구현력 기르기 - 06] 정다면체

# 풀이과정 -> 성능측정결과, 답안이 더 빠름
import time
start_time = time.time()

def polyhedron(N, M):
    sum_list=[]
    for i in range(1,N+1):
        for n in range(1,M+1):
            sum_list.append(i+n)
    unique_list= list(set(sum_list))
    defult=0
    for i in unique_list:
        if sum_list.count(i)>defult:
            defult = sum_list.count(i)
    for i in unique_list:
        if sum_list.count(i)==defult:
            print(i, end=' ')
            return None
polyhedron(100, 200)

end_time = time.time()
print("성능 측정:", end_time - start_time)

# 답안
start_time = time.time()
def polyhedron(n, m):
    cnt=[0]*(n+m+3)
    max=-6667643
    for i in range(1, n+1):
        for j in range(1,m+1):
            cnt[i+j]+=1
    for i in range(n+m+1):
        if cnt[i]>max:
            max=cnt[i]
    for i in range(n+m+1):
        if cnt[i] == max:
            print(i, end=' ')
            return None
polyhedron(100, 200)
end_time = time.time()
print("성능 측정:", end_time - start_time)



### [02.코드 구현력 기르기 - 07] 자릿수의 합

# 풀이과정 -> 성능측정결과, 답안이 더 빠름
import time
import random

N = int(input())
n_list = list(input().split())

start_time = time.time()
def digit_sum(N, n_list):
    max_num = 0
    max_dev = 0
    for i in n_list:
        num = 0
        for n in i:
            num+=int(n)
        if num > max_dev:
            max_num = i
            max_dev = num
    return print(max_num)
digit_sum(N, n_list)
end_time = time.time()
print("성능 측정:", end_time - start_time)

# 답안
n = int(input())
a = list(map(int, input().split()))

start_time = time.time()

def digit_sum(x):
    sum=0
    for i in str(x):
        sum+=int(i)
    return sum

max=-21470000000
for x in a:
    tot=digit_sum(x)
    if tot>max:
        max=tot
        res=x
print(res)
end_time = time.time()
print("성능 측정:", end_time - start_time)



### [02.코드 구현력 기르기 - 08] 소수의 개수 (에라토스테네스 체)

# 풀이과정 -> 내 풀이과정이 더 간결
number = 0
for i in range(2,21):
    for n in range(2,21):
        if i==n: continue
        if i%n == 0:
            break
    else: number += 1
print(number)

# 답안
n=int(input())
ch=[0]*(n+1)
cnt=0
for i in range(2,n+1):
    if ch[i]==0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j]=1
print(cnt)



### [02.코드 구현력 기르기 - 09] 뒤집은 소수

# 풀이과정 -> 내 풀이과정이 더 간결
def reverse(x):
    return x[::-1]

def isPrime(x):
    x = int(x)
    for i in range(2,x+1):
        if i == x: continue
        if x%i == 0: break
    else: return x

N = int(input())
n_list = list(input().split())

for i in n_list:
    value = isPrime(reverse(i))
    if value: print(value, end=' ')

# 답안
def reverse(x):
    res = 0
    while x>0:
        t = x%10
        res = res*10+t
        x = x//10
    return res

def isPrime(x):
    if x == 1:
        return False
    for i in range(2, x//2+1):
        if x%i == 0:
            return False
    else:
        return True

n = int(input())
a = list(map(int, input().split()))
for x in a:
    tmp = reverse(x)
    if isPrime(tmp):
        print(tmp, end=' ')
