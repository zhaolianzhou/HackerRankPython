import math
def diaDiffer(n,arr):
    dia1=0
    dia2=0
    for i in range(n):
        dia1+=arr[i][i]
        dia2+=arr[i][n-i]
    return math.fabs(dia1-dia2)
