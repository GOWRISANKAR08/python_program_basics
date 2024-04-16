string = input("Enter a String : ")
alphabets=0
digits=0
specialChars=0
#checks for each character in the string
for i in string: 
	#if character of the string is an alphabet
    		if i.isalpha():
       			 alphabets+=1
		#if character of the string is a digit
    		elif i.isdigit():
        			digits+=1
    		else: #if character of the string is a special character
        			specialChars+=1
print("alphabets =",alphabets,"digits =",digits,"specialChars =",specialChars)
