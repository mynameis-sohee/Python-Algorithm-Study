```python
def solution(array, commands):
    answer = []
    for x in commands:
        i, j, k = x[0], x[1], x[2]
        new_arr = array[i-1:j]
        new_arr.sort()
        ans = new_arr[k-1]
        answer.append(ans)
    return answer
```

다른 풀이
```python
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```
