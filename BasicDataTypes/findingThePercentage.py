if __name__ == '__main__':
    n = int(raw_input())
    student_marks = {}
    for _ in range(n):
        line = raw_input().split()
        name, scores = line[0], line[1:]
        scores = map(float, scores)
        student_marks[name] = scores
    query_name = raw_input()
    sum=0
    n=len(student_marks[query_name])
    curr_score=student_marks[query_name]
    for s in curr_score:
        sum+=s
    print ("{0:.2f}".format(sum/n))