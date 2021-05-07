'''
종류: 파이썬 내장함수 Map 에러
에러: TypeError: map() must have at least two arguments.
원인: 파이썬 map은 기본적으로 데이터 처리를 str로 처리. 따라서, int로 지정하길 원하면 int 선언 필요
'''

## 에러코드

def solution(num):
    num_square = list(map(lambda x: x*x, num) )
    print(num_square)

    answer=[]
    for i in num_square:
        if i % 2 == 0:
            answer.append("짝수")
        else:
            answer.append("홀수")
    print(answer)

num = map(input().split(',') )
solution(num)


## 해결코드

def solution(num):
    num_square = list(map(lambda x: x*x, num) )
    print(num_square)

    answer=[]
    for i in num_square:
        if i % 2 == 0:
            answer.append("짝수")
        else:
            answer.append("홀수")
    print(answer)

num = map(int, input().split(',') )
solution(num)
