def insertionSort(ar):
    n = len(ar)
    # for i in range(n-1):
    #     curr_index = i+1
    #     curr_num = ar[curr_index]
    #     j = curr_index + 1
    #     if j == n:
    #         break
    #     while j < n:
    #         if ar[j] < curr_num:
    #             ar[j-1] = ar[j]
    #         else:
    #             ar[j-1] = curr_num
    #             break
    #         if j==n-1:
    #             ar[j] = curr_num
    #         j+=1
    for i in range(n-1):
        curr_index = i+1
        curr_num = ar[curr_index]
        j = curr_index - 1
        if j < 0:
            break
        while j > -1:
            if ar[j] > curr_num:
                ar[j+1] = ar[j]
            else:
                ar[j+1] = curr_num
                break
            if j==0:
                ar[j] = curr_num
            j -= 1
        for item in ar:
            print(item, end=' ')
        print()
    return

ar = [1, 4, 3, 5, 6, 2]
insertionSort(ar)