def solution(prices):
    answer = []
    length = len(prices)
    
    for i in range(length):
        for k in range(i,length):
            if prices[i] > prices[k]:
                answer.append(k-i)
                break
        else:
            answer.append(length-i-1)
    return answer
