n= input()
s=0
rem = 0
while n!=0:
   rem = n % 10
   s= s + rem
   n = n//10
print ("sum of digit",s)
   