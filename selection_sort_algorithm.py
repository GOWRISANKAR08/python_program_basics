l=[2,1,4,6,3]
for i in range(len(l)-1):
    min_index = i
    for j in range(i+1,len(l)):
        if l[j]< l [min_index]:
            min_index=j
    l[i],l[min_index]=l[min_index],l[i]
print(l)