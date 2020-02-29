from gpiozero import LED
from signal import pause

red = LED(4)
yellow = LED(17)
green = LED(23)

#red.blink()
yellow.blink()
#green.blink()

pause()
