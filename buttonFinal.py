import time
import neopixel
import board
from gpiozero import Button

#Setting Button
button = Button(23)

#LED Pin Setup
pixel_pins = board.D18
num_pixels = 16
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pins, num_pixels, brightness = 0.2, auto_write = False, pixel_order = ORDER)

#Color Keys
Cyan = '1'
Purple = '2'
Yellow = '3'
Red = '4'

#Button Function
def buttonPress():
	print("I am pressed")
#	f = open("incoming.txt", "r")
#	g = open("outcoming.txt", "r")
	h = open("state.txt", "w+")
#	incomingColor = f.read()
#	h.write('1')
#	g = open("outcoming.txt", "w+")
#	g.write(incomingColor)
	g = open("outcoming.txt", "r")
	outcomingColor = g.read()
	print(outcomingColor)

	if(outcomingColor == Cyan):
		pixels.fill((255, 0, 255))
		pixels.show()
	if(outcomingColor == Purple):
		pixels.fill((255, 255, 0))
		pixels.show()
	if(outcomingColor == Yellow):
		pixels.fill((255, 0, 0))
		pixels.show()
	if(outcomingColor == Red):
		pixels.fill((0, 255, 255))
		pixels.show()

	button.wait_for_release()
	g = open("outcoming.txt", "r")
	outcomingColor = g.read()
	num = int(outcomingColor)
	newColor = str(num+1)
	print(newColor)
	g = open("outcoming.txt", "w+")
	if(outcomingColor == Red):
		g.write('1')
	else:
		print("hit")
		g.write(newColor)
	h.write('1')

while(True):
	if(button.is_pressed):
		buttonPress()
