def check_palindrome(word):
    start=0
    end=len(word)-1
    while start< end:
        if word[start]!=word[end]:
            return 0
        start+=1
        end-=1
    return 1

def remove_punc(word):
    s=''
    for letter in word:
        if letter.isalpha():
            s+=letter
    return s
    

f=open('D:/python/read.txt','r')
f2=open('D:/python/palindrome_check.txt','w')
s=f.readline()
while s:
    for word in s.split():
        word=remove_punc(word)
        if check_palindrome(word):
            f2.write(word+'\n')
    s=f.readline()
f.close()
f2.close()