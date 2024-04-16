n=input("enter the string: ")
vowels = 0
consonent= 0
vow='aeiouAEIOU'
for i in range(len(n)) :
    if n[i] in vow:
    #  if n[i] in 'aeiouAEIOU':
        vowels = vowels + 1
    else:
        consonent = consonent + 1

print("vowels : ",vowels)
print("consonent : " ,consonent)