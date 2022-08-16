import time
import neopixel
import board

#Adafruit files and credentials
from Adafruit_IO import Client, Feed, Data, RequestError
ADAFRUIT_IO_KEY ='IMPORT KEY'
ADAFRUIT_IO_USERNAME = 'IMPORT USER'
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

#LED Pin Setup
pixel_pins = board.D18
num_pixels = 16
ORDER = neopixel.GRB
pixels = neopixel.NeoPixel(pixel_pins, num_pixels, brightness = 0.2, auto_write = False, pixel_order = ORDER)

#Setting Color Keys
Cyan = '1'
Purple = '2'
Yellow = '3'
Red = '4'

#Reads incoming net data, sends to incoming
def read_write():

	##Polling data
	dataAddress = aio.feeds('distance-lamp')
	dataReceive = aio.receive(dataAddress.key)
	color = dataReceive.value

	##Writing data to incoming
	f = open("incoming.txt", "w+")
	f.write(color)

	##Reading incoming, outcoming, and state
	f = open("incoming.txt", "r")
	g = open("outcoming.txt", "r")
	h = open("state.txt", "r")
	incomingColor = f.read()
#	print(incomingColor)
	outcomingColor = g.read()
	state = h.read()
#	print(state)
	##Writing over incoming or outcoming depending on contents

	##If the state is set to 0(no change or net change), it changes the outcoming to match the incoming
	if((incomingColor!=outcomingColor) and (state=='0')):
		print("hit1")
		g = open("outcoming.txt", "w+")
		g.write(incomingColor)
		if(incomingColor == Cyan):
			pixels.fill((0, 255, 255))
			pixels.show()
		if(incomingColor == Purple):
			pixels.fill((255, 0, 255))
			pixels.show()
		if(incomingColor == Yellow):
			pixels.fill((255, 255, 0))
			pixels.show()
		if(incomingColor == Red):
			pixels.fill((255, 0, 0))
			pixels.show()
		print("hit2")

	##If the state is set to 1(local change), it changes the incoming to match the outcoming again
	if(state == '1'):
#		print("hit3")
		f = open("incoming.txt", "w+")
		f.write(outcomingColor)
#		time.sleep(1)
		f = open("incoming.txt", "r")
		print(f.read() + " Incoming Text")
		print(outcomingColor + " Outcoming Text")
		h = open("state.txt", "w+")
		h.write('0')
		h = open("state.txt", "r")
		print(h.read() +" State Variable")
#		print("hit4")
		write_send()
	time.sleep(1)
#Reads outcoming file and sends data to net if change is 1
def write_send():
	#Polling Data
	dataAddress = aio.feeds('distance-lamp')
	dataReceive = aio.receive(dataAddress.key)
	g = open("outcoming.txt", "r")
	h = open("state.txt", "r")
	outcomingColor = g.read()
	state = h.read()
	print(state)
	aio.send_data(dataAddress.key, outcomingColor)
	aio.append(dataAddress.key, outcomingColor)


while(True):
	read_write()
	time.sleep(1)
#	write_send()
#	time.sleep(1)
