import sys,os
def romanizer(numbers):
    result = []
    for num in numbers:
        curr_roman = helper(num)
        result.append(curr_roman)
    return result

def helper(num):
    res = ''
    while num>0:
        if num-1000>=0:
            res+='M'
            num-=1000
        elif num-900>=0:
            res+='CM'
            num-=900
        elif num-500>=0:
            res+='D'
            num-=500
        elif num-400>=0:
            res+='CD'
            num-=400
        elif num-100>=0:
            res+='C'
            num-=100
        elif num-90>=0:
            res+='XC'
            num-=90
        elif num-50>=0:
            res+='L'
            num-=50
        elif num-40>=0:
            res+='XL'
            num-=40
        elif num-10>=0:
            res+='X'
            num-=10
        elif num-9>=0:
            res+='IX'
            num-=9
        elif num-5>=0:
            res+='V'
            num-=5
        elif num-4>=0:
            res+='IV'
            num-=4
        elif num-1>=0:
            res+='I'
            num-=1
    return res