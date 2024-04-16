def make_decorator(func): #decorator function
    def inner():            #wrapper function
        print('its decorator')
        func()
    return inner
@make_decorator
def ordinary():
    print('iam ordinary')

# dec_fun = make_decorator(ordinary)    #inner == dec_func
# dec_fun()       




# divide the number which is greater by smaller

def smart_div(func):
    def inner(a,b):
        if b>a:
            a,b=b,a
        return func(a,b)
    return inner

@smart_div
def div(a,b):
    return a/b
print(div(10,2))
print(div(2,10))
# dec = smart_div(div)  #without decorator
