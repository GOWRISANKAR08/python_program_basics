def sum_of_runs(l):
    s=0
    for i in range(len(l)):
        s+=l[i]
    return s

def average(l):
    return sum_of_runs(l)/len(l)
    

runs = [('rohit',234),('kohli',254),('rohit',34),('rohit',34),('kohli',54),('kohli',24)]
d={}
for player,score in runs:
    # if player not in d.keys():
    #     d[player]=[]     #creating key with empty list value
    try:
        d[player].append(score)
    except KeyError:            # key not found
        d[player]=[]            # creating key with empty list
        d[player].append(score)
        
print(d)
print(sum(d['rohit']))
print(sum_of_runs(d['kohli']))
print(average(d['kohli']))