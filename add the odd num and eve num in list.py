l=[1,7,8,5,2]
odd=0
even=0

for i in range(len(l)):
    if l[i]%2 == 0:
        even=even+l[i]
    else:
         odd=odd+l[i]
print("sum of odd num is: ",odd)
print("sum of even num is: ",even)

       