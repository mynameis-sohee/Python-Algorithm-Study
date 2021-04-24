#sort 함수를 호출하면 안 됨
#sort:n*log(n)
#sort되어 있는 경우 n번만에 가능

#리스트들 요소를 포인터에 따라서 하나씩 비교함
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

p1=p2=0
c = []
while p1<n and p2<m:
    if a[p1] <=b[p2]:
        c.append(a[p1])
        p1+=1
    else:
        c.append(b[p2])
        p2+=1
if p1<n:
    c=c+a[p1:]
if p2<m:
    c=c+b[p2:]
for x in c:
    print(x, end=' ')