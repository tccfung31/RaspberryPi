from sense_hat import SenseHat
import time
import datetime
import MySQLdb

try:
    from sense_hat import SenseHat
except ImportError:
    from sense_emu import SenseHat

sense = SenseHat()


def get_temp():
    temp = sense.get_temperature()
    print("The temperature is: ", temp)
    return temp


def get_humi():
    humi = sense.get_humidity()
    print("The humidity is: ", humi)
    return humi


def get_press():
    press= sense.get_pressure()
    print("The pressure is: ", press)
    return press



#db = MySQLdb.connect("localhost", "root", "raspberry", "mydb")
# db = MySQLdb.connect("localhost", "root", "raspberry", "mydb")
#cursor = db.cursor()

while True:
    
    for event in sense.stick.get_events():
# Check if the joystick was pressed
       if event.action=="pressed": 
        if event.direction == "down":
            db = MySQLdb.connect("192.168.1.95", "root", "raspberry", "mydb")
            cursor = db.cursor()
            currentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO trainingdb1 (rec_time, rec_temp, rec_humi, rec_press) VALUES (%s, %s, %s, %s)"
            val = (currentT, get_temp(), get_humi(), get_press())
        elif event.direction == "up":
            db = MySQLdb.connect("localhost", "root", "raspberry", "mydb")
            cursor = db.cursor()
            currentT = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            sql = "INSERT INTO EVMR1 (rec_time, rec_temp, rec_humi, rec_press) VALUES (%s, %s, %s, %s)"
            val = (currentT, get_temp(), get_humi(), get_press())
    # val = ("56046680", get_temp(), get_humi(), get_press())
        cursor.execute(sql, val)
        db.commit()
    time.sleep(1)
    sense.clear()
