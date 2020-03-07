from gpiozero import Button
from signal import pause

button = Button(21)

def elo():
	print("xdddddd")

button.when_pressed = elo

pause()
