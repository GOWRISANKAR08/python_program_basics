# n=4
# for i in range (n):
#     for j in range(n):
#         print('* ',end ='') #end is a default in program it means start a new line we change into empty string end = " "
#     print()

############################################

#print using space

# n=4
# start = n-1
# for i in range(n):
#     for j in range (n):                         #   *  *  *  *
#         if j<= start:                           #   *  *  *
#             print('*  ',end='')                 #   *  *
#         else:                                   #   *
#             print("   ",end='')                 
#     print()
#     start -= 1

#############################################3
# program prymid using alphabet

# n=4
# start = 0
# alph = 'abcdefghijklmnopqrstuvwxyz'
# for i in range(n):
#     for j in range (n):                       
#         if j<= start:                           
#             print(alph[i],end='')                
#         else:                                   
#             print("   ",end='')                 
#     print()
#     start += 1


########################################
# prymid

# n=4
# start = n-1
# end = n-1
# for i in range(n):
#     for j in range (n*2-1):                       
#         if j>= start and j<=end:                           
#             print('*',end='')                
#         else:                                   
#             print(" ",end='')                 
#     print()
#     start -= 1
#     end +=1
    
    ###############################
    # inverted prymid
    
# n=4
# start = n-4
# end = n+2
# for i in range(n):
#     for j in range (n*2-1):                       
#         if j>= start and j<=end:                           
#             print('*',end='')                
#         else:                                   
#             print(" ",end='')                   
#     print()
#     start += 1
#     end -=1


##################################3
# daimond


# n=7
# start = n//2
# end = n//2
# for i in range(n):
#     for j in range (n):                       
#         if j>= start and j<=end:                           
#             print('*',end='')                
#         else:                                   
#             print(" ",end='')                   
#     print()
#     if i< n//2:
#         start -= 1
#         end +=1
#     else:
#         start+=1
#         end -=1
        
        
##############################
#right side dimond

# n=7
# start = n-4
# for i in range(n):
#     for j in range (n-3):                       
#         if j>= start:                           
#             print('*',end='')                
#         else:                                   
#             print(" ",end='')                   
#     print()
#     if i< n-4:
#         start -= 1
#     else:
        # start+=1
################################3
# using single loop

# n=int(input())              #value based method
# for i in range(n):
#     print((n-(i+1))* " " +'*'*(i+1) )
#         # or
        
# n=int(input())
# star = 1
# space = n-1
# for i in range(n):
#     print(' '*space + "*"* star)
#     star+=1
#     space -=1
    
###################################
#box
n=7
row =1 
column = n-2

for i in range(n):
    for j in range(n):
    #   if i==0 or j==0 or i==n-1 or j==n-1:
        if ((i == 0 or i == n-1)): #or  i + j == n-1):
          print('*',end='')
        elif row==i and column ==j:
           print('*',end='')    
           row +=1
           column -=1 
        else:
          print(' ',end='')
    print()
    

    