def bubbleSort(lst):
    tamLst = len(lst)
    for i in range(tamLst):
        for j in range((tamLst - i)-1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                
    return lst

print(bubbleSort([3,1,7,4,9,2,5]))