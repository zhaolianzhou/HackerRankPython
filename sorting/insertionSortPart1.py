#!/bin/python
def insertionSort(ar):
    n = len(ar)
    tem = ar[n-1]
    i = n-2
    while i>-1:
        if ar[i] > tem:
            ar[i+1] = ar[i]
        else:
            ar[i+1] = tem
            break
        for item in ar:
            print(item, end=' ')
        print()
        if i==0:
            ar[i]=tem
        i-=1
    for item in ar:
        print(item, end=' ')
    return

# m = input()
# ar = [int(i) for i in input().strip().split()]
ar = [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]
insertionSort(ar)