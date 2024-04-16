s= 'hello aaiioubc abz zz'
count = 0
max_count = 0

for val in s:
    if val.lower() in 'aeiou':
        count +=1                   #if given strins=g in the vowel it should increment the count value
    
    else:
        if count > max_count:       # count greaterthan maxcount
            max_count = count       #assign count value into maxcount
        count = 0                   # the reset the count value into 0
print(max_count)