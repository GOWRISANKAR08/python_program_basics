#BUBBLE SORT / ADJACENT ALGORITHM

l=[2,1,4,5,3]
n=len(l)
for i in range (n-1):
    swap = False
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1] = l[j+1],l[j]
            swap = True
        if swap == False:
            break
print(l)