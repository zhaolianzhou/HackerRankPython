result = []
scores = []
for _ in range(int(raw_input())):
    name = raw_input()
    score = float(raw_input())
    result.append([name,score])
    scores.append(score)
cur_min = min(scores)
scores = [val for val in scores if val!=cur_min]
second_min = min(scores)
name=[]
for res in result:
    if res[1]==second_min:
        name.append(res[0])
name = sorted(name)
for nam in name:
    print nam