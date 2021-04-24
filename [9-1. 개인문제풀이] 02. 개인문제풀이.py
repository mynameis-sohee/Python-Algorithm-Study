# 문제 이해 못함 ㅠ.ㅠ

#입국심사
def solution(n, times):
    answer = 0

    leng = len(times)
    left = 1
    right = (leng+1) * max(times) # 최대 범위

    while left <= right:
        mid = (left + right) // 2

        count = 0
        for time in times:
            count += mid // time
            # 심사 인원수를 넘으면 다음 단계
            if count >= n: break

        # n명을 심사 할 수 있는 경우
        # 한 심사관에게 주어진 시간을 줄여본다.
        if count >= n:
            answer = mid
            right = mid - 1
        # 없는 경우
        elif count < n:
            left = mid + 1
    return answer
    
    #징검다리
    def solution(distance, rocks, n):
    answer = 0
    rocks.append(distance) 
    rocks.sort()
    left, right = 0, distance
    while left <= right:
        mid = (left + right) // 2  
        min_distance = float('inf')  # 각 mid 에서 최솟값
        current = 0  # 현재 위치
        remove_cnt = 0  # 바위를 제거한 개수
        
        # 거리 재기
        for rock in rocks:
            diff = rock - current  # 바위와 현재 위치 사이의 거리
            if diff < mid:  # mid 보다 거리가 짧으면 바위 제거
                remove_cnt += 1
            else:  # mid 보다 거리가 길거나 같으면 바위 그대로 두고
                current = rock  # 현재 위치를 그 바위로 옮기고
                min_distance = min(min_distance, diff)  # 해당 mid 단계에서의 최소거리인지 체크
        
        # mid를 설정하는 단계
        if remove_cnt > n:  # 바위를 너무 많이 제거한 경우 mid 줄이기
            right = mid - 1
        else:  # 바위를 너무 적게 제거한 경우 또는 딱 맞는 경우 mid를 늘려서 바위를 더 제거하거나 mid의 최댓값을 올려보기
            answer = min_distance
            left = mid + 1
        
    return answer
