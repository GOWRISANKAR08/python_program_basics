            ##################DICTIONARY#################

d={'name':'main','age':17}

#accessing value
print(d[('age')])
print(d.get(1))   #either this or that method

#adding / update items

d['lacation']='chennai'
d.update({'address':'velachery'})
d.update({'age':17})

print(d)
d['address']='thambaram'
d['age']=d['age'] +2
# d['age']+=2         #this or that
print(d)

#remove items
d.pop('name')
del d["location"]
print(d)

# print(d.keys())
# print(d.values())
# print(d.items())




#iterating  dict value
# for i in d.keys():      # 1st method
#     print(d[i])

# for i in d.values():    #2nd mathod
#     print(i)
    
# for key,val in d.items():   #3 rd method
#     print(val)