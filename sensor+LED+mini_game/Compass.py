from sense_hat import SenseHat
from time import sleep

sense = SenseHat()


def showori (dir):
    sense.clear()
    sense.show_letter(dir[0].upper(),text_colour=[255,0,0])

while True:

  o=sense.get_orientation()
  
  yaw=o["yaw"]

  if yaw < 45 or yaw >= 315:
    dir = 'north'
    showori(dir)

  elif yaw >=45 and yaw < 135:
    dir = 'east'
    sense.set_rotation(180)
    showori(dir)

  elif yaw >= 135 and yaw < 225:
    dir = 'south'
    sense.set_rotation(270)
    showori(dir)

  elif yaw >=225 and yaw < 315:
    dir = 'west'
    sense.set_rotation(270)
    showori(dir)
