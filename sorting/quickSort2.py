def quick_sort2(A):
    if len(A)==0:
        return []
    if len(A)==1:
        return A
    else:
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
        sorted_left = quick_sort2(a_left)
        sorted_right = quick_sort2(a_right)
        current_sorted = sorted_left+a_equal+sorted_right
        for item in current_sorted:
            print(item, end=' ')
        print()
        return current_sorted



# m = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
ar=[5,8,1,3,7,9,2]
result = quick_sort2(ar)