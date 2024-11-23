#jackson Vaughn
#Program to display data on the LCD screen
#!/usr/bin/env python3

#Imports
import time 
import LCDDriver as LCD    
from datetime import datetime

LCD.setup()
#Clear screen 
LCD.clear()

try:
	while True:
		
		#the top of the screen should be flowing stock prices

		#Display date & time at the bottom of the scree 
		now = datetime.now()
		Curdate = str(now.strftime("%m-%d-%Y %H:%M:%S"))
		
		LCD.write(Curdate,LCD.LINE_2)
		time.sleep(1)



		LCD.clear()

except KeyboardInterrupt:
	LCD.clear()
	LCD.write("Good bye!",LCD.LINE_1)
	time.sleep(0.5)
	LCD.clear()
	print("exit")