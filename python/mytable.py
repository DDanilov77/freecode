#import os      #os.mkdir("newdir")     #os.chdir("/home/newdir")
import MySQLdb
from PyQt5.QtWidgets import QMainWindow, QApplication

f = open("mysql.conf", "r")
ipaddress=f.readline()
user=f.readline()
password=f.readline()
database=f.readline()
f.close()

conn = MySQLdb.connect(ipaddress, user.strip(), password.strip(), database.strip())
cursor = conn.cursor()

cursor.execute("SELECT FromHost, COUNT(*), MIN(ReceivedAt), MAX(ReceivedAt) FROM `SystemEvents` GROUP BY `FromHost` ORDER BY `MAX(ReceivedAt)`")

# Получаем данные.
row = cursor.fetchone()
#print(row)
count=0
f = open("mydata.txt", "w+")

for row in cursor:
        count=count+1
        print("№: ",count,"Server: ",row[0]," Count logs: ",row[1]," Start: " ,row[2]," End: ", row[3])
        f.writelines(str(row))

f.close()
# Разрываем подключение.
conn.close()

#next query
