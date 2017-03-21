import re
def count_substring(string, sub_string):
    index = [i for i in range(len(string)) if string.startswith(sub_string,i)]
    return len(index)

s = 'ABCDCDC'
sub = 'CDC'
print count_substring(s,sub)