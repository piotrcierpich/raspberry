from gpiozero import LED
from time import sleep

red = LED(4)
yellow = LED(17)
green = LED(23)

while True:
	red.on()
	print('czerwony')
	sleep(3)
	
	yellow.on()
	print('żółty')		
	sleep(1)
	red.off()	
	yellow.off()
	
	green.on()
	print('zielony')
	sleep (3)
	green.off()
	
	yellow.on()
	print('żółty')
	sleep(1)
	yellow.off()
	
