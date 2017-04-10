def countSorting(N,A):
    count = [0]*100
    for i in range(N):
        count[A[i]]+=1
    for i in range(100):
        print(count[i],end=' ')

# N = int(input().strip())
# ar = [int(i) for i in input().strip().split()]
ar = [1,2,3,4,3,6,7]
N=7
countSorting(N,ar)