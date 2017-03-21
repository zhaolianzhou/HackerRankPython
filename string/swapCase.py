def swap_case(s):
    result = ''
    for c in s:
        if c.isupper():
            result+=c.lower()
        else:
            result+=c.upper()
    return result