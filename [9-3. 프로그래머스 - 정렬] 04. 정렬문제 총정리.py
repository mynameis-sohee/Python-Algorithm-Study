# 첫 번째 문제
def solution(array, commands):
    answer = []
    for i in commands:
        answer_list = array[i[0]-1:i[1]]
        answer_list.sort()
        answer.append(answer_list[i[2]-1])
    return answer



# 두 번째 문제
# 오답노트: str의 우선순위는 ascii 값에 의거하여 순차적으로 비교해 지정된다.
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return ''.join(numbers)


  
 # 세 번째 문제
def solution(citations):
    for i in range(len(citations),0, -1):
        cnt = 0
        for k in citations:
            if k>=i:
                cnt += 1
        if cnt == i :
            return i 
            
