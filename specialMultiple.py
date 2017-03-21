import re
n = int(raw_input())
nums = []

for i in range(n):
    num_item = int(raw_input())
    nums.append(num_item)

def findz(num):
    z = 0
    mul = num
    num2 = 0
    num5 = 0
    while mul>1:
        if mul%2==0:
            num2+=1
            mul/=2
        if mul%5==0:
            num5+=1
            mul/=5
    mul=num
    mul_str = str(mul)
    ismatch = re.match(r'[4]*[0]*',mul_str)
    if ismatch is not None:
        a = 0
        b = 0
        for c in mul_str:
            if c=='4':
                a+=1
            elif c == '0':
                b+=1
        z = 2*a + b

    return z

for i in range(n):
    z= findz(nums[i])
    print z