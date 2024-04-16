# import math as m   #alias name
# import factorial_modules as m1
# n=2
# print(m.sqrt(6))
# print(m1.factorial(5))
# help(math.sqrt)

# def s(b,a):
#     '''this function return factorial'''
#     return a+b
# # help(s)
# print(s.__doc__)   # print a comented document line
# print(s(1,2))


# print("you're welcome")
# print('you\'re welcome')
# print('c:\\')

def add(*args): #Non-keyword
    s = 0
    for i in range(len(args)):
        s+=args[i]
    print(args) #data in Tuple
    return s

print(add(5,6,4,8,5,56))

def phone_book(**kwargs):   #keyword argument
    print(kwargs)   #data saved as dict

phone_book(name='Kumar',phone='9898983293',address='Chennai')



def sample(a,b,*values,**pairs):        #all in one  non-keyword ,kewords and first 2 arguments are necessary argument
    print('fixed args: ',a,b)
    print('Non-Keyword args: ',values)
    print('Keyword args: ', pairs)

sample(1,3,4,4,6,6,6,4,name='Kumar',phone='9898983293',address='Chennai')