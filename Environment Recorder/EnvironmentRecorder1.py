from sense_hat import SenseHat
import time
import datetime
import MySQLdb


def get_temp():
    temp = sense.get_temperature()
    print("The temperature is: ", temp)
    return temp

def get_humi(): #function of get humidity
    humi = sense.get_humidity()
    print("The humidity is: ", humi)
    return humi

def get_pres(): #function of get pressure
    pres = sense.get_pressure()
    print("The pressure is: ", pres)
    return pres


db = MySQLdb.connect("localhost", "root", "raspberry", "mydb")
cursor = db.cursor()

sense = SenseHat()
sense.clear()

while True:
    currentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    sql = "INSERT INTO EVMR1 (rec_time, rec_temp,rec_humi,rec_press) VALUES (%s, %s, %s, %s)"
    val=  (currentT,get_temp(),get_humi(),get_pres())
    

    cursor.execute(sql,val)
    db.commit()

    time.sleep(2)

db.close()
