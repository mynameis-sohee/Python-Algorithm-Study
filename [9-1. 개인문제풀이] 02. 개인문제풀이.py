### 이진탐색 구현

def search(num, sample):
    start_index = 0
    end_index = len(sample) - 1
    while start_index<=end_index:
        mid = (start_index+end_index)//2 # 몫 출력
        if sample[mid] == num:
            return mid
        elif sample[mid] > num:
            end_index = mid-1 # 이 부분 -1 유의
        else: start_index = mid+1 # 이 부분 +1 유의
    return None
    
print(search(2, [2, 3, 5, 7, 11]))



### sort 알고리즘 정리

# 선택정렬: 각 위치에 어떤 값이 들어갈지 찾는 방법 - 정렬 상황에 영향을 받지 않고 일정 시간이 소요됨
# 삽입정렬: 각 값이 어떤 위치에 들어갈지 찾는 방법 - 이미 거의 정렬되었을 경우 유용
# 힙정렬: 무작위 순서 리스트 정렬 시 유용
# 기타 정렬: https://www.toptal.com/developers/sorting-algorithms


### 좋은 코드의 기준
# 1. 시간 2. 공간
