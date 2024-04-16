
import mysql.connector as sql
import matplotlib.pyplot as plt
connection = sql.connect(user='root',
            password='gowrisankar@88',
            host='localhost',
            database='world')   #open connection
c = connection.cursor()
# c.execute('SELECT name,population FROM city order by population desc limit 5;')
c.execute('SELECT CountryCode,population FROM city where CountryCode = "IND;')
l=c.fetchall()
print (l)
x,y = [],[]
for city,population in l:
    x.append(city)
    y.append(population)
    print(x)
    print(y)
plt.bar(x,y)
plt.ylabel('population')
plt.xlabel('city')
plt.title('top 5 ciities population')
plt.show()
