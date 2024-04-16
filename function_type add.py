# def add(a,b):
#     print(a+b)
# add(2,5)

# # def add(a):
# #     return a+5
# # print(add(2))
# # result=add(6)
# # print(result)

# #power
# def add(a,b):
#     print("power",a**b)
# add(2,5)



# maximum

# def maximum(l):
#     m=l[0]
#     for i in range (len(l)):
#         if l[i]>m:
#             m=l[i]
#     return m
# l=[2,7,8,10,20]

# print(maximum(l))
# print(max(l))


# sum of element
# def sum(l,s):

#     for i in range (len(l)):
#         s=s+l[i]
#     return s
# l=[2,7,8,10,20]
# s=0
# print(sum(l,s))



#-----------------RECURSIVE----------------------

#factorial using recursion

# def factorial(n):
#     if n==1:   #base condition
#         return 1
#     else:
#         return n*factorial(n-1)  #recursive condition
    
# print(factorial(5))



#-----------------------------
#fibinocci using recursion


def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1) + fib(n-2)
n=6
print(fib)


        