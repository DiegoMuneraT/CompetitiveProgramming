#pip install mysql-connector-python

import mySQL
import mysql.connector

con = mysql.connector.connect(host='127.0.0.1', user='root', passwd='test', db='sakila')

cur = con.cursor()

cur.execute("SELECT * FROM ACTOR LIMIT 10")

num_field = len(cur.description)
field_name = [i[0] for i in cur.description]
print(str(num_field)," ", field_name)

cur.fetchall()

cur.close()
con.close()