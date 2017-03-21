
import sys


n = int(raw_input().strip())
for a0 in xrange(n):
    grade = int(raw_input().strip())
    # your code goes here
    if grade < 38:
        print grade
    else:
        if grade%5>=3:
            round_g = grade+(5-grade%5)
            print round_g
        else:
            print grade