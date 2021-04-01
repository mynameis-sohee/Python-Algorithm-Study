### 팔린드롬 문제

def is_palindrome(word):
    if word == word[::-1]:
        return 'True'
    else: return 'False'

# 테스트
print(is_palindrome("racecar"))



### 선형탐색 문제

def linear_search(element, some_list):
    for i in range(0,len(some_list)):
        if some_list[i] == element:
            return i

# 테스트
print(linear_search(2, [2, 3, 5, 7, 11]))
