'''
문제: 작은 값 2개를 더해 새로운 값을 만들어 추가하는 문제. 큐+순서O => 힙!
아이디어: hq 라이브러리 활용
소요시간: 20분
풀이결과: 스스로 진행, 81점 (1.3.8.14 런타임 에러)
'''

import heapq as hq

def solution(scoville, K):
    
    hq.heapify(scoville)
    answer = 0

    while True:
        n = hq.heappop(scoville)
        if n < K:
            n_1 = hq.heappop(scoville)
            hq.heappush(scoville, n+(n_1*2))
            answer += 1
        else:
            break
    
    return answer
