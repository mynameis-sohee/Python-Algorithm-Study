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

