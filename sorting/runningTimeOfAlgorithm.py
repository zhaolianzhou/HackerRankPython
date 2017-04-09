def insertion_sort(l):
    shift = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
           l[j+1] = l[j]
           shift+=1
           j -= 1
        l[j+1] = key
    return shift