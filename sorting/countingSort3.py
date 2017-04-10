def countSorting(N,A):
    count = [0]*100
    sums = [0]*100
    for i in range(N):
        count[A[i][0]]+=1
    sums[0]=count[0]
    for i in range(1,100):
        sums[i]=sums[i-1]+count[i]
        Num_con = count[i]

    for j in range(100):
        print(sums[j],end=' ')

N = int(input().strip())
ar = list()
for i in range(N):
    index,content = input().strip().split()
    ar.append((int(index),content))
# ar = [1,2,3,4,3,6,7]
# N=7
countSorting(N,ar)