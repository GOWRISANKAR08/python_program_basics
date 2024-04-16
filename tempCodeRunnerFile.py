c.execute('SELECT name,population FROM city order by population desc limit 5;')
c.execute('SELECT CountryCode,population FROM city where CountryCode = "IND;')
l=c.fetchall()
print (l)
x,y = [],[]
for CountryCode , population in l:
    x.append(CountryCode)
    y.append(population)
    print(x)
    print(y)