
# row=3
# column=3
# m1=[[1,2,3],[4,5,6],[7,8,9]]
# m2=[[2,4,6],[3,1,7],[8,9,5]]
# m3=[0,0,0],[0,0,0],[0,0,0]
# for r in range(row):
#     for c in range(column):
#         m3[r][c]=m1[r][c]+m2[r][c]
# print(m3)

# m1=[[1,2,3],[4,5,6],[7,8,9]]
# m2=[[2,4,6],[3,1,7],[8,9,5]]
# m3=[0,0,0],[0,0,0],[0,0,0]
# for r in range(len(m1)):
#     for c in range(len(m1[0])):
#         m3[r][c]=m1[r][c]+m2[r][c]
# print(m3)

# m1=[[1,2,3],[4,5,6],[7,8,9]]
# m2=[[2,4,6],[3,1,7],[8,9,5]]
# m3=[]
# for r in range(len(m1)):
#     m3.append([])
#     for c in range(len(m1[0])):
#         print(m3)
#         m3[r].append(m1[r][c]+m2[r][c])
# print(m3)

##############################################

#adding two matrix

r1 = int (input())
c1= int(input())
m1=[[int(i)for i in input().split()] for r in range(r1)]  #list comprehension
# m1=[]
# for i in range (r1):
#     m1.append([int(i)for i in input().split()])
# print(m1)
r2=int(input())
c2=int(input())
m2= [[int(i)for i in input().split()] for r in range(r2)]  #list comprehension
# m2=[]
# for i in range (r2):
#     m2.append([int(i)for i in input().split()])
if r1==r2 and c1==c2:
    m3= [[m1[r][c]+m2[r][c] for c in range (len(m1[0]))] for r in range(len(m1))]   #list comprehension
    print(m3)
else:
    print('matrix is not posible')

##############################################
# multiple of matrix

# m3=[]
# if c1==r2:
#   for r in range(r1):
#     m3.append([])
#     for c in range(c2):
#       s=0
#       for k in range(c1):
#         s+=m1[r][k]*m2[k][c]
#       m3[r].append(s)
#       print(m3)
# else:
#   print('matrix not possible')
  
  
  
  
