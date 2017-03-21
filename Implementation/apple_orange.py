import sys


s,t = raw_input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = raw_input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = raw_input().strip().split(' ')
m,n = [int(m),int(n)]
apple = map(int,raw_input().strip().split(' '))
orange = map(int,raw_input().strip().split(' '))

ap_house = 0
or_house = 0
for i in range(m):
    if apple[i]+a >= s and apple[i]+a<=t:
        ap_house+=1
for j in range(n):
    if orange[j]+b<=t and orange[j]+b>=s:
        or_house+=1
print ap_house
print or_house