s = int(input())
start= 0
end = len(s)- 1
flag= 1
while start<end:
    if s[start]!=s[end]:
       # print(" not palindrome")
       flag= 0
       break
    start +=1 # incrementing the value
    end -=1 #decrement the value of index
if flag == 1:
    print('palindrome')
else:
    print(" notpalindrome")
    
    
    
    