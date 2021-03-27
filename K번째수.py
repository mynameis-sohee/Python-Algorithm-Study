t = int(input())

list1 = []
for i in range(t):
    n, s, e, k = map(int, input().split())
    
for j in range(n): #여기..
    list1 = list(map(int, input().split()))


for listt in list1:
    listt =listt[s-1:e-1]
    listt.sort()

for i in range(len(list1)):
      print(f'#{i}', list1[i][k])