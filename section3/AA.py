#앞에서 읽으나 뒤어서 읽으나 같으면 YES 출력
#회문 문자열 아니면 NO 출력
#대소문자 구분 안 함

n = int(input())

for i in range(n):
    strings = input()
    strings = strings.lower()
    reversed_string = "".join(reversed(strings))
    if strings == reversed_string:
        print(f'#{i+1} YES')
    else:
        print('#{i+1} NO')


######면접 볼 때는 이렇게 해야 함
n = int(input())

for i in range(n):
    strings = input()
    strings = strings.upper()
    size = len(strings)
    for j in range(size//2):
        if strings[j] != strings[-1-j]:
            print("#%d NO" %(i+1))
            break
        else:
            print("#%d YES" %(i+1))

###문자열 거꾸로해서 풀기
### 파이썬스럽게
n = int(input())

for i in range(n):
    strings = input()
    strings = strings.upper()
    if strings == strings[::-1]:
        print("#%d NO" %(i+1))
    else:
        print("#%d YES" %(i+1))