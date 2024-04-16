# n=5
# for n in range(n):
#     for j in range(n):
        
#         print(j,end='')
#     print()
    
#     # n = 9

# # for n in range(1, n+1):

# #     for m in range(1, n + 1):

# #         print(m, end=’ ’‘)

#     print(“”)

# n=4
# start = 0
# for i in range(n):
#     for j in range (n):                         #   *  *  *  *
#         if j>= start:                           #   *  *  *
#             print('*  ',end='')                 #   *  *
#         else:                                   #   *
#             print("   ",end='')                 
#     print()
#     start = 1

# n=4
# start = n-1
# end = n-1
# for i in range(n):
    
#     for j in range (n*2-1):                       
#         if j>= start and j<=end:                          
#             print(i+1,end='')  
#             j= i+1
                    
#         else:                                   
#             print(" ",end='') 
#             j=1
            
           
                            
#     print()
#     start -= 1
#     end +=1

# n=4
# start = n-1
# end = n-1
# s=1
# for i in range(n):
#     for j in range (n*2-1):                       
#         if j>= start and j<=end:                          
#             print(s,end='')  
#             s= s+1        
#         else:                                   
#             print(" ",end='') 
#             s=1                   s
#     print()
#     start -= 1
#     end +=1
    
# l1=['hub','python']
# for i in l1:
#     l1.append(i.upper())
#     break
# print(l1)


# n=5

# for row in range (n):
# 	for col in range (n):
# 		if (row == col):
# 			print("2 ", end=" ")
# 		else:
# 			print("0 ", end=" ")
# 	print()


a=int(input())
b=int(input())
print(a+b)