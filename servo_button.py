from gpiozero import Servo
from time import sleep
from gpiozero import Button
from signal import pause


button=Button(26)
servo=Servo(5)

def friend():
	servo.max()
	print("max")
	
def bye():
	servo.min()
	print("min")
	
button.when_released = bye 	
button.when_pressed = friend

pause()
