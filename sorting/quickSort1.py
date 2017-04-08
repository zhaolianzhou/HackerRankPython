def quick_sort1(A):
    a_left = []
    a_right = []
    a_equal = []
    middle = A[0]
    for item in A:
        if item > middle:
            a_right.append(item)
        elif item < middle:
            a_left.append(item)
        else:
            a_equal.append(item)
    return a_left+a_equal+a_right



m = int(input().strip())
ar = [int(i) for i in input().strip().split()]
# ar=[4,6,1,3,5,2]
result = quick_sort1(ar)
for item in result:
    print(item, end=' ')