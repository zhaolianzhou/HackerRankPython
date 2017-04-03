import sys


n = int(input().strip())
height = [int(height_temp) for height_temp in input().strip().split(' ')]

def heightNo(n, height):
    max_height = None
    height_count = dict()
    for item in height:
        if item in height_count:
            height_count[item]+=1
        else:
            height_count[item]=1
        if max_height is None or max_height < item:
            max_height = item

    return height_count[max_height]