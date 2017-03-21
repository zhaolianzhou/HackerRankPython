import sys
x1,v1,x2,v2 = raw_input().strip().split(' ')
x1,v1,x2,v2 = [int(x1),int(v1),int(x2),int(v2)]
if v1==v2 and x1!=x2:
    print "NO"
elif v1==v2 and x1==x2:
    print "YES"
elif abs(x1-x2)%abs(v1-v2)==0 and (x1-x2)/(v2-v1)>0:
    print "YES"
else:
    print "NO"