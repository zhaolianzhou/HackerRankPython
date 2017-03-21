
import sys,math


n,m = raw_input().strip().split(' ')
n,m = [int(n),int(m)]
a = map(int,raw_input().strip().split(' '))
b = map(int,raw_input().strip().split(' '))

def LCM(nums):
    factors = dict()
    for num in nums:
        for i in range(int(math.sqrt(num))+1):
            if num%i == 0:
                factors[i]=1
                factors[num/i]=1