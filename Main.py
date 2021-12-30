from datetime import datetime
import time
from plyer import notification
import mysql.connector

now = datetime.now()
current_hour = now.strftime("%H")
current_min = now.strftime("%M")

mydb=mysql.connector.connect ( host = "localhost", user= "root", password="2980", database="test")
mycursor=mydb.cursor()

mycursor.execute("select * from t3")
myres = mycursor.fetchall()
print(myres)

for msg in range(0,1):
    finres = list(myres[msg])
    print(finres)
    titlep = finres[0]
    messagep = finres[1]
    phour = finres[2]
    pmin = finres[3]
    print(current_hour, phour, current_min, pmin)
    
    if current_hour == phour and current_min == pmin:
        notification.notify(
            title = titlep,
            message = messagep,
            app_icon = "D:\Task Scheduler/alert.ico",
            timeout = 20
            )
 
