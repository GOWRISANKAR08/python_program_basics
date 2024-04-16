try:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    print(a+b)
except:
    print('enter integer only')
    
'''##################'''

try:
    a = int(input('enter a: '))
    b = int(input('enter b: '))
    print(a/b)
    tuple = (1,25,4)
    tuple[0]=3
except ZeroDivisionError:
    print('we can\'t divide a number by 0')
except ValueError:
    print('enter integer only')
except Exception as e:   
    print(e)
except:
    print('something went wrong')
else:
    print('else block is executed')   #without any error means the elsew block will executed
finally:
    print("finally is executed")   # error or whatever the fillay block will executed it called regards od exception handling