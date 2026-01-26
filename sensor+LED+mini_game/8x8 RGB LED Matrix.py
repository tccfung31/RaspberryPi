from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
blue = (0, 0, 255)
yellow = (255, 255, 0)

sense.clear(blue) #set all the pixels to same color
sleep(5)
sense.clear(yellow)
sleep(5)
sense.clear()