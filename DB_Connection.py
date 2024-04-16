import mysql.connector as sql
connection = sql.connect(user='root',
            password='gowrisankar@88',
            host='localhost',
            database='world')   #open connection
c = connection.cursor()
c.execute('SELECT * FROM city;')
d = {}
l = c.fetchall()    #get data from DB
for id,city,cc,district,population in l:
    if cc not in d.keys():
        d[cc] = []  #creating new key
    d[cc].append(city)
print(d['IND']) #getting indian cities name from dict
c.execute('CREATE TABLE employee3 (name VARCHAR(50));')
connection.commit()     #commit make changes in DB


connection.close()  #close connection
