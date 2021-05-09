#문자열에서 숫자만 추출하여 자연수와 자연수의 약수의 개수 출력

s = input()

res = 0
for x in s:
    if x.isdecimal():
        res = res*10+int(x)
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(res)
print(cnt)