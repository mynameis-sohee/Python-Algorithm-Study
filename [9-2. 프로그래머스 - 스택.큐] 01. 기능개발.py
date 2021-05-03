'''
문제: 리스트 내 데이터 값마다 우선순위가 존재하는 문제 - pop 을 떠올리자!
아이디어: 앞 숫자에서 n값을 곱하는 행위와, count하는 행위를 나누어서 수행하도록 코드를 구현한 반면, 다른 사람의 문제풀이는 한 번에 해당 행위들을 수행하도록 설계했다. (if 활용)
소요시간: 1시간
풀이결과: 스스로 진행, 정답
'''

# 풀이과정
from collections import deque

def solution(progress, speeds):
    stack = deque([])

    for i in range(len(progress)):
        cnt = 0
        while progress[i] < 100:
            progress[i] += speeds[i]
            cnt += 1
        stack.append(cnt)

    cnt = 1
    answer = []
    max_num = stack.popleft()

    while stack:
        if max_num >= stack[0]:
            cnt += 1
            stack.popleft()
        else:
            answer.append(cnt)
            cnt = 1
            max_num = stack.popleft()
    answer.append(cnt)
    return answer

  
# 다른 사람 풀이과정
def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                print(answer)
                count = 0
            time += 1
    answer.append(count)
    print(answer)
    return answer

# 테스트 샘플  
solution([93, 30, 55],[1, 30, 5])
