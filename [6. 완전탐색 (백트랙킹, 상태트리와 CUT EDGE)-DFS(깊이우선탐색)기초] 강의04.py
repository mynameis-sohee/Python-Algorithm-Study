
### [06. Dynamic Programming(동적계획법) - 04]  합이 같은 부분집합
'''
핵심: 1회 출력 후 함수 실행 종료 위해, sys 라이브러리 사용
난이도: 중상, 풀이 안 보고 직접 풀었으며 정답!

풀이 시 중요한 것: 부분집합1 더한 값과 그렇지 않은 집합 합이 같다는 조건은, sum = total-sum 으로 두면, 필요치 않은 변수를 추가 생성하지 않아도 된다.

※ 아직 해설강의 X

'''

import sys

def DFS(x):
  if x == n:
    sum_gr_1 = 0
    sum_gr_2 = 0
    for i in range(1,n+1):
      if ch[i] == 1:
        sum_gr_1 += nums[i-1]
      else:
        sum_gr_2 += nums[i-1]

    if sum_gr_1 == sum_gr_2:
      print('YES')
      # 한번 실행 후 종료
      sys.exit()
      
  else:
    ch[x] = 1
    DFS(x+1)
    ch[x] = 0
    DFS(x+1)

def SYS(x):
  answer = DFS(x)
  if answer is None:
    print('No')
  

if __name__ == '__main__':
    n=int(input())
    nums = list(map(int, input().split()) )
    ch = [0]*(n+1)
    SYS(1)
    
    


# 정답
import sys
def DFS(L, sum):
  if sum>total//2:
    return
  if L==n:
    if sum==(total-sum):
      print('YES')
      sys.exit(0)
  else:
    DFS(L+1. sum+a[L])
    DFS(L+1, sum)

if __name__=='__main__':
  n=int(input())
  a=list(map(int, input().split()))
  total=sum(a)
  DFS(0,0)
  print('NO')
