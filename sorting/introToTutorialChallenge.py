num = int(raw_input().strip().split(' '))
n = int(raw_input().strip().split(' '))
arr = map(int,raw_input().strip().split(' '))
for i in range(n):
    if arr[i]==num:
        print i