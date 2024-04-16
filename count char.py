s= input("enter a string:")
alphabet = 0
digit = 0
special_char = 0
vow='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
all_digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
for i in range (len(s)):
    if s[i] in vow:
        alphabet +=1
    elif s[i] in all_digits:
            digit +=1
    else:
            special_char +=1
print("alphabet in srting: ",alphabet)
print("digit in string: ",digit)
print("special character in a string: ",special_char)

