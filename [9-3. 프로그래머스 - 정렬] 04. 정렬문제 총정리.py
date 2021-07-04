# 첫 번째 문제
def solution(array, commands):
    answer = []
    for i in commands:
        answer_list = array[i[0]-1:i[1]]
        answer_list.sort()
        answer.append(answer_list[i[2]-1])
    return answer

print(solution(array, commands))




# 두 번째 문제
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
            
