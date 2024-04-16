import mysql.connector as sql
import matplotlib.pyplot as plt
connection = sql.connect(user='root',
            password='gowrisankar@88',
            host='localhost',
            database='world')   #open connection
c = connection.cursor()
# c.execute('SELECT name,population FROM city order by population desc limit 5;')
# c.execute('SELECT Code,population FROM country where Code in("IND","AFG","AUS","USA") ;')
c.execute(""" SELECT 
    CASE 
        WHEN Code IN ('IND', 'AFG', 'CHN', 'USA') THEN Code
        ELSE 'Others' 
    END AS CountryCode,
    SUM(population) AS TotalPopulation
FROM 
    country
GROUP BY 
    CASE 
        WHEN Code IN ('IND', 'AFG', 'CHN', 'USA') THEN Code
        ELSE 'Others' 
    END;
""")
l=c.fetchall()
print (l)
x,y = [],[]
for CountryCode , population in l:
    x.append(CountryCode)
    y.append(population)
    print(x)
    print(y)
plt.pie(y,labels=x)
plt.show()