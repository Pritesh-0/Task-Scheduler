import mysql.connector
mydb=mysql.connector.connect ( host = "localhost", user= "CurrentUser(Default root)", password="YourPassword", database="YourDatabaseName")
mycursor=mydb.cursor()
title1 = input("Enter Your Task Title : ")
message1 = input("Enter Your Task Message : ")
hour = input("Enter Your Task Time(Hour) : ")
minute = input("Enter Your Task Time(Minutes) : ")

sql="insert into t3 (title,message,remh,remm) values(%s,%s,%s,%s)"
val=(title1,message1,hour,minute)
mycursor.execute(sql,val)
mydb.commit()
