def bubble(list):
    for _ in range(len(list)-1):
        for i in range(len(list)-1):
            cnt += 1
            if list[i] > list[i+1]:
                swap1 = list[i]
                swap2 = list[i+1]
                list[i] = swap2
                list[i+1] = swap1
    return list

# print(bubble([2,1,6,7,4,5]))
