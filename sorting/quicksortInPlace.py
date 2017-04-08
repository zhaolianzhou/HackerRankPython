def quick_sort_inplace(A,lo,hi):
    if lo < hi:
        p=lomuto_partition(A,lo,hi)
        quick_sort_inplace(A,lo,p-1)
        quick_sort_inplace(A,p+1,hi)



def lomuto_partition(A, lo,hi):
    pivot = A[hi]
    i = lo-1
    for j in range(lo,hi):
        if A[j]<=pivot:
            i+=1
            tem = A[i]
            A[i] = A[j]
            A[j] = tem
    tem = A[i+1]
    A[i+1] = A[hi]
    A[hi] = tem
    for item in A:
        print(item, end=' ')
    print()
    return i+1


# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
ar=[1 ,3 ,9, 8, 2, 7, 5]
result = quick_sort_inplace(ar,0,len(ar)-1)
