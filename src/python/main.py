#jackson Vaughn
#Program to display data on the LCD screen
#!/usr/bin/env python3

#Imports
import time 
import LCDDriver as LCD    
from datetime import datetime
import GetPrice
import json

#Basic function to setup the LCD
def main():
    now = datetime.now()
    CurTime = str(now.strftime('%m-%d %H:%M:%S'))
    print(f'Starting up at {CurTime}')
    LCD.setup()
    while True:
        LCD.write('Hello',LCD.LINE_2)

if __name__ == '__main__':
    main()
