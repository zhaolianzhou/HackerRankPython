def countSorting(N,A):
    count =dict()
    for i in range(100):
        count[i] =list()
    sums = [0]*100
    half = int(N/2)
    result = list()
    for i in range(half):
        count[A[i][0]].append('-')
    for i in range(half,N):
        count[A[i][0]].append(A[i][1])
    for j in range(100):
        curr_list = count[j]
        for item in curr_list:
            print(item, end=' ')

# N = int(input().strip())
# ar = list()
ar = [(0,'ab'),(6,'cd'),(0,'ef'),(6,'gh'),(4,'ij'),(0,'ab'),(6,'cd'),(0,'ef'),(6,'gh'),(0,'ij'),(4, 'that'),
      (3, 'be'),(0,'to'),(1,'be'),(5, 'question'),(1, 'or'),(2, 'not'),(4, 'is'),(2,'to'),(4,'the')]
# for i in range(N):
#     index,content = input().strip().split()
#     ar.append((int(index),content))
countSorting(20,ar)