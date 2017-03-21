from __future__ import division
import sys
# n = int(input().strip())
# arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
n =4
arr=[4,3,-2,0]
def plusMinus(n,arr):
    if n == 0:
        return 0.000000,0.000000,0.000000
    pos = neg = zero = 0
    for num in arr:
        if num > 0:
            pos+=1
        elif num==0:
            zero+=1
        else:
            neg+=1
    pos = pos/n
    neg = neg/n
    zero = zero/n
    return pos,neg,zero

pos, neg, zero = plusMinus(n,arr)
print("{0:.6f}".format(pos))
print("{0:.6f}" .format(neg))
print("{0:.6f}" .format(zero))