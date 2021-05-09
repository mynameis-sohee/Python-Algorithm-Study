#오름차순으로 한 줄로 놓여있는 20장의 카드에 대해
#10개의 구간이 주어지면 주어진 구간의 순서대로
#처리한 후 마지막 카드들의 배치르 구하라

a, b = map(int, input().split())
#스와프
a, b = b, a 

a = list(range(21))
for _ in range(10):  #_언더바: 변수가 없는 거
    s, e = map(int, input().split())
    for i in range((e-s+1)//2):
        a[s+i], s[e-i] = a[e-i], a[s+i]
a.pop(0)
for x in a:
    print(x, end= ' ')
