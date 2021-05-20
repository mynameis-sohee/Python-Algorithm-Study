DFS 방식으로 풀어야하는 문제?
현재까지 푼 문제 중에서는 (점수, 걸리는 시간) 이런식으로 조건이 짝지어있는 경우가 많았다.

예시1) N개의 문제를 풀려고 할 때 각 문제는 그것을 풀었을 때 얻는 점수와 푸는데 걸리는 시간이 주어지게 된다. 
제한시간 M안에 N개의 문제를 풀어 얻을 수 있는 최대점수는?

예시2) 일을 할 때 받을 수 있는 금액과 걸리는 시간이 주어져있을 때, 
제한된 기간 내에서 최대로 받을 수 있는 금액은?

예시1)
![image](https://user-images.githubusercontent.com/73813367/118907093-e16a4c80-b959-11eb-96e0-a037c4dc9232.png)

```python
#DFS(레벨, 총점, 시간)
import sys
sys.stdin= open("in5.txt", "r")
def DFS(L, sum, time):
    global res 
    if time > m: #가지치기
        return

    if L == n:
        if sum > res:
            res = sum
    else:
        DFS(L+1, sum+pv[L], time + pt[L]) #문제 풀었을 때 #왼쪽 노드
        DFS(L+1, sum, time) #문제 안 풀었을 때 # 오른쪽 노드

if __name__ == '__main__':
    n, m = map(int, input().split())
    pv = list()
    pt = list()
    for i in range(n):
        a, b = map(int, input().split())
        pv.append(a)
        pt.append(b)
    res = -21470000000
    print(DFS(0,0,0))
```
