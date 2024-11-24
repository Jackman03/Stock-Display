#jackson Vaughn
#LCD Driver for the HD44708 I2C
#!/usr/bin/env python3
import time
import smbus

#This is a amalgamation of youtube tutorials.

#need to possibly redo this to allow for scrolling.

#The address the LCD lives on, this may vary.
#do i2cdetect -y 1 to find this address and change it here
#going to try and automate this in a setup script
ADDR = 0x27

#The screen is 16 units long
SCREEN_WIDTH = 16

#Send data is 1 and send a commmand is 0
DATA = 1
CMD = 0	

#RAM addresses for the lines
LINE_1 = 0x80
LINE_2 = 0xC0
LINE_3 = 0x94
LINE_4 = 0xD4

BACKLIGHT = 0x08

ENABLE = 0b00000100

DELAY = 0.0005
PULSE = 0.0005

#create the data bus
BUS = smbus.SMBus(1)

#Function to setup the LCd
def setup():
	#read the datasheet thay said...
	send_byte(0x33,CMD)	#sets up 4 bit mode
	send_byte(0x32,CMD)	#ensure 4 bit mode is active
	send_byte(0x06,CMD)	#cursor move to the right
	send_byte(0x0C,CMD)	#display on, cursor off, blink off
	send_byte(0x28,CMD)	#more 4 bit config
	send_byte(0x01,CMD)	#clear display
	time.sleep(DELAY)
		


#This functions sends the byte data to the LCD
def send_byte(bits,mode):
	#mode is 0 for command and 1 for data
	
	#sets the first 4 bits into high mode.
	high = mode | (bits & 0xF0) | BACKLIGHT
	#sets the 4 bits into low mode
	low = mode | ((bits<<4) & 0xF0) | BACKLIGHT
	
	#Set into high mode
	BUS.write_byte(ADDR,high)
	enable(high)
	
	#Set into low mode
	BUS.write_byte(ADDR,low)
	enable(low)
	
def enable(bits):
	time.sleep(DELAY)
	#enable the pins high. btiwire or with the enable bits
	BUS.write_byte(ADDR,(bits | ENABLE))
	time.sleep(PULSE)
	#disables the pin. sets the enable bit to 0 so the lcd can reset 
	BUS.write_byte(ADDR,(bits & ~ENABLE))
	#allows the LCD to proccess the lasst operation
	time.sleep(DELAY)
	
#function to write data to the screen.
def write(message,line):
	#pads the rest of the message with blank chars
	message = message.ljust(SCREEN_WIDTH," ")
	
	#write the the specfic line
	send_byte(line,CMD)
	
	for i in range(SCREEN_WIDTH):
		#sends the ascii value of each char
		send_byte(ord(message[i]),DATA)

#Sends the clear signal to clear the screen	
def clear():
	send_byte(0x01,CMD)
	


