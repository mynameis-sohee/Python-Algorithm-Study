## 내가 푼 답
```python

n, k = map(int, input().split())


nlist = list(map(int, input().split()))

from itertools import combinations

#숫자 3개 뽑아 합

comb_list = list(combinations(nlist, 3))
#print(comb_list)
sum_list = []
for tuples in comb_list:
    summ = sum(tuples)
    sum_list.append(summ)

sum_list = set(sum_list)
#print(sum_list)
sum_list = list(sum_list)
sum_list.sort(reverse=True)
print(sum_list[k-1])
```
## 모범 답안
```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
res = set()
for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            res.add(a[i]+a[j]+a[m])

res=list(res)
res.sort(reverse=True)
print(res[k-1])
```

## 새로 배운 점
1. set 구조에 입력! :add
2. set = list(set) :set을 list로 만들기
3. itertools 없이 재귀함수로 combination 구현

```python
def sum_of_comb(array, c):
    return list(combinations(array, c))
def n_length_comb(array, c):
    if c == 0:
        return [[]]
    
    comb_list = []
    for i in range(0, len(array)):
        m = array[i]
        remlst = array[i+1:]

        for p in n_length_comb(remlst, c-1):
            comb_list.append([m]+p)

    return comb_list

#driver code
#if __name__ == "__main__":
 #   arr = "abc"
  #  print(n_length_comb([x for x in arr], 3))
```
