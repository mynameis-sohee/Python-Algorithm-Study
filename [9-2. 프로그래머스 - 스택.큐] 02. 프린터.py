from collections import deque

def solution(priorities, location):
    priorities = deque(enumerate(priorities))
    cnt = 0
    while True:
        max_num = max(priorities, key= lambda x : x[1])[1]
        num = priorities.popleft()
        if num[1] != max_num:
            priorities.append(num)
        else:
            cnt += 1
            if num[0] == location:
                answer = cnt
                break
    return answer
