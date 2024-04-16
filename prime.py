n=int(input())
prime= 1
for i in range (2,n):
    if n%i==0:
        # print(n ,",is not a prime")
        prime=0
        break
if prime==1:
    print("num is prime")
else:
    print("not a prime")
# else:
#     print(n,"is prime")