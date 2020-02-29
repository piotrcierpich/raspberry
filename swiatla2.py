from gpiozero import LED
from time import sleep

red = LED(4)
yellow = LED(17)
green = LED(23)

def switch(led, sleepTime, color):	
	led.on()
	print(color)
	sleep(sleepTime)
	led.off()

while True:
	red.on()
	print('czerwony')
	sleep(3)	
	yellow.on()		
	print('zolty')
	sleep(1)
	red.off()	
	yellow.off()
	
	switch(green, 3, 'zielony')
	switch(yellow, 1, 'zolty')	
