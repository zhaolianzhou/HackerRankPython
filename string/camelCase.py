import sys
s = raw_input().strip()
result = 1
for i in s:
    if i.isupper():
        result+=1
print result