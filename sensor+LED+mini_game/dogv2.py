from sense_hat import SenseHat
sense = SenseHat()
sense.clear()
r = (255, 102, 102) #red
b = (51, 153, 255) #blue
w = (200, 200, 200) #white
y = (204, 204, 0) #yellow
e = (0, 0, 0) #empty
dog = [
e, e, e, e, e, e, e, e,
r, e, e, e, e, e, e, e,
e, r, e, e, r, e, r, e,
e, r, b, b, r, y, y, e,
e, b, b, b, y, w, y, b,
e, b, b, b, b, y, y, e,
e, e, b, e, b, e, e, e,
e, e, e, e, e, e, e, e
]
sense.set_pixels(dog)
sense.flip_h()