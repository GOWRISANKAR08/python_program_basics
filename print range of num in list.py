# def list1(start,end,step):
#     l=[]
#     while start < end:
#         l.append(start)
#         start+= step
#     return l
# print(list1(1,10,1)) 

def list1(end,s=0,st=0):
    l=[]
    while s < end:
        l.append(s)
        s+= st
    return l
print(list1(10,1,2)) 
