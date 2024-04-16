import random as r
lottery_no = r.randint(1, 100)
no_of_chance = 5
while no_of_chance > 0:
    n=int(input('guess no: '))
    if n == lottery_no:
        print('congrats u won the lottery')
        break
    elif n>lottery_no:
        print('num is greather than lottery')
    else:
        print('num is lessthan than lottery')
    no_of_chance -=1
else:
    print('sorry your chance is exahusted')
    print("lotterr no is: ",lottery_no,'\n BETTERLUCK NEXT TIME')