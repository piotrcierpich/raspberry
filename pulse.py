from gpiozero import PWMLED
from signal import pause

red = PWMLED(4)
yellow = PWMLED(17)
green = PWMLED(23)

red.pulse()
yellow.pulse()
green.pulse()

pause()
