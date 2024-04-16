f=open('D:/python/read.txt','r')
# s1=f.read()
# vowel=0
# for i in s1:
#     if i in 'aeiouAEOIU':
#         vowel+=1
# print("vowel count:",vowel)

# print(f.readline())   # read a 1st line initilize
# print(f.readline())
# print(f.readline())

# s= f.readline()   #read a 1st line 
# v=0
# while s:
#     # print(s)
#     for i in s:
#         if i in "AEIOUaeiou":
#             v+=1
        
    
#     s=f.readline()   #read a 2nd line
# print('vowel count: ',v)
# f.close()
    
    
    
    ################################################
    
#write  a file
# f=open('D:/python/read.txt','w+')

# f.write('new sheet')
# f.close()
# f=open('D:/python/read.txt','r+')
# print(f.read())
# f.close()

    ################################################
    
#write  a file
# f=open('D:/python/read.txt','a+')  #adding a new line 

# f.write('\nwelcome')
# f.close()

###################################33
# palindrome
s= f.readline()   #read a 1st line 


while s:
    # print(s)
    s.split()
    start=0
    end = len(s)-1
    
    while start<end:
        if s[start]!=s[end]:
            break
    start +=1 # incrementing the value
    end -=1 #decrement the value of index
if flag == 1:
    
else:
    print(" notpalindrome")

        
    
    s=f.readline()   #read a 2nd line
print('vowel count: ',v)
f.close()
    
