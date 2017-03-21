def mutate_string(string, position, character):
    string = string[:position]+character+string[position+1:]
    l = list(string)
    l[position]=character
    l=''.join(l)
    return l