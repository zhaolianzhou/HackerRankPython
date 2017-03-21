s = raw_input()
if len(s)==0:
    print "Empty String"
else:
    ns=''
    n = len(s)
    i = 0
    while i < n:
        if i==n-1:
            ns+=s[i]
            i+=1
            continue
        if s[i] == s[i + 1]:
            i += 2
        else:
            ns += s[i]
            i += 1
    while ns!=s:
        s = ns
        ns = ''
        n = len(s)
        i=0
        while i < n:
            if i == n - 1:
                ns += s[i]
                i += 1
                continue
            if s[i] == s[i + 1]:
                i += 2
            else:
                ns += s[i]
                i += 1
    if len(ns)==0:
        print "Empty String"
    else:
        print ns