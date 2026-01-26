from sense_hat import SenseHat
import time
import datetime
import MySQLdb


def get_temp():
    temp = sense.get_temperature()
    print("The temperature is: ", temp)
    return temp



db = MySQLdb.connect("localhost", "root", "raspberry", "mydb")
cursor = db.cursor()

sense = SenseHat()
sense.clear()

while True:
    currentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO training2 (rec_time, rec_temp) VALUES (%s, %s)"
    val=  (currentT,get_temp())
    

    cursor.execute(sql,val)
    db.commit()

    time.sleep(2)

db.close()
