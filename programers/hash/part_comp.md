프로그래머스 코딩테스트 연습
https://programmers.co.kr/learn/courses/30/lessons/42576

## 첫 번째 풀이
```python
def solution(participant, completion):
    for i in participant:
        if i not in completion:
            answer = i
        if (participant.count(i) > 1) & (participant.count(i) > completion.count(i)):
            answer = i
    return answer
```
결과: 테스트 케이스 통과했다고 해서 제출했는데, 두번째 테스트에서 시간초과됨

테스트 1 〉	통과 (0.01ms, 10.2MB)
테스트 2 〉	통과 (0.04ms, 10.2MB)
테스트 3 〉	통과 (10.42ms, 10.3MB)
테스트 4 〉	통과 (40.09ms, 10.5MB)
테스트 5 〉	통과 (39.02ms, 10.5MB)
