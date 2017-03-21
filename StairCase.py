def StairCase(n):
    result = list()
    for i in range(n):
        curr_str = ' '*(n-i-1)+'#'*(i+1)
        result.append(curr_str)
        print curr_str
    return result


result = StairCase(6)
print result