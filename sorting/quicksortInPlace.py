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

def quick_sort_inplace(A,lo,hi,swap):
    if lo < hi:
        p,swap=lomuto_partition(A,lo,hi,swap)
        swap = quick_sort_inplace(A,lo,p-1,swap)
        swap = quick_sort_inplace(A,p+1,hi,swap)
    return swap



def lomuto_partition(A, lo,hi,swap):
    pivot = A[hi]
    i = lo-1
    for j in range(lo,hi):
        if A[j]<=pivot:
            i+=1
            swap+=1
            tem = A[i]
            A[i] = A[j]
            A[j] = tem
    tem = A[i+1]
    A[i+1] = A[hi]
    A[hi] = tem
    swap+=1
    # for item in A:
    #     print(item, end=' ')
    # print()
    return i+1,swap



# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
ar1=[1 ,3 ,9, 8, 2, 7, 5]
ar2=list(ar1)
result = quick_sort_inplace(ar1,0,len(ar1)-1,0)
shift = insertion_sort(ar2)
print(shift-result)