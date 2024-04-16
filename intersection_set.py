#sum logic

# l=[1,23,45,88]
# s=0
# for i in range (len(l)):
#     s=s+l[i]
# print(s)

# dynamic input
# l=['hat','mat','cat','bat']
# s=set(l[0])  #convert into set
# for i in range (len(l)):
#     s=s & set(l[i])
# print(s)


###########################3
# user input
n=int(input())
l=[input()for i in range(n)] # list comprehension
# l=[]
# for i in range(n):
#     s=input()
#     l.append(s)

s=set(l[0])  #convert into set
for i in range (len(l)):
    s=s & set(l[i])
print(s)



###############################


