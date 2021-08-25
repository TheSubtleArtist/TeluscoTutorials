#Includes 73
#MySQL Workbench Setup; Python Database Connection
#How to install the connector
#pip3 install mysql connector

import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", passwd='M3L0V3Pu$$yT@5ti', database="sakila") #pass username, password, database name, and IP address

mycursor = mydb.cursor() #create a variable to pass arguements to mySQL
actorcursor = mydb.cursor()


mycursor.execute("show databases") #stores the names of all databases in mycursor, which is now a list
for i in mycursor:
    print(i)

actorcursor.execute("select * from actor") #pulls data from the table "actor"
for i in actorcursor:
    print(i)