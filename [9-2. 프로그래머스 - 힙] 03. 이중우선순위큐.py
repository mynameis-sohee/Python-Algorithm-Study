'''
문제: 조건에 따라 최소값, 최대값을 삭제하거나 값을 추가하는 문제. 값 추가+숫자의 크기(최소or최대)에 따른 값 삭제 => 힙!
아이디어: heapq.heapify 를 활용하고, 최대.최소값 삭제를 위해 튜플을 활용(기능을 넣긴 했지만, 없어도 잘 돌아감...최적 코드 구글링 필요)
소요시간: 40분
풀이결과: 스스로 진행, 100점
'''
import heapq as hq

def solution(operations):
    answer = []
    hq.heapify(answer)
    num = 0

    for i in operations:
        i = i.split(' ')
        if i[0] == 'I':
            hq.heappush(answer, int(i[1]) )
            num += 1
        else:
            if answer:
                answer.sort()
                if i[1] == '1':
                    answer.pop()
                else:
                    hq.heappop(answer)
    answer.sort()
    if answer:
        return [answer[-1],answer[0]]
    else:
        return [0,0]
