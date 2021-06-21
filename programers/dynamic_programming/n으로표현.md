문제 출처: https://programmers.co.kr/learn/courses/30/lessons/42895 <br>
풀이 출처: https://gurumee92.tistory.com/164

## 문제 풀이 전략

* 5를 1번 사용해서 만들 수 있는 수: 5 (1번 set)
* 5를 2번 사용해서 만들 수 있는 수: 55, 5+5, 5-5, 5*5, 5//5 (2번 set)  <br>
                               = 5를 연속으로 이어 붙인 수, 1번 set과 1번 set의 사칙연산

* 5를 3번 사용해서 만들 수 있는 수: 5를 연속으로 이어 붙인 수, 1번 set과 2번 set의 사칙연산, 2번 set과 1번 set의 사칙연산

### N을 n번 사용해서 만들 수 있는 수
N을 연속으로 이어 붙인 수, 1번 set과 n-1 번 set의 사칙연산, 2번 set과 n-2번 set의 사칙연산.....n-1번 set과 1번 set의 사칙연산

## 문제 풀이 
1~8까지 순회해서 만들어지는 수들의 집합 속에 number가 있는 최소의 수 구하기 (최솟값이 8을 넘어가면 -1이니까 8까지만 순회함)

1. set이 8개인 리스트 초기화
2. 각각의 set에 N을 연속으로 이어 붙인 수를 넣음 ex) 5, 55, 555...
3. 숫자 N에 대해서 n개를 사용해 표현한 수의 일반화 수식을 코드로 표현
4. for i in range(1, 8): #1에서 8까지 순회
5.    for j in range(i): # 
6.    j개를 사용해서 만든 수들의 집합 s[j]를 다음과 같이 순회
7.    i-j-1 을 사용해서 만든 수들의 집합 s[i-j-1]를 다음과 같이 순회
8.    option1(s[j] set)과 option2(s[i-j-i] set)을 사칙연산
9.    사칙연산한 값을 집합 s[j]에 추가
10.   만약 number가 s[j]에 있으면 s[i+1] 반환
11.8번 순회 후에 number를 못 찾면 -1 반환 
```python
def solution(N, number):
    answer = -1

    memo = [set() for x in range(8)] 
    
    for idx, sett in enumerate(memo,start=1): #0,1,2,3...7
        sett.add(int(str(N)*idx))
    
    # 숫자 N에 대해 n개를 사용해 표현한 수의 일반화 코드
    for i in range(1,9): 
        for j in range(i):
            #s[j] 구하기 #j가 1일 때
            for op1 in memo[j]:
                for op2 in memo[i-j-1]:
                    #사칙연산
                    memo[i].add(op1+op2)
                    memo[i].add(op1-op2)
                    memo[i].add(op1*op2)
                    if op2 != 0:
                        memo[i].add(op1//op2)
        
        if number in memo[i-1]:
            answer = i 
            break
    #else:
     #   answer = -1

    return answer
  
if __name__ == "__main__":
    
    result = solution(5,12)
    print(result)
```
