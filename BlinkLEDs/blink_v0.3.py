from gpiozero import LED
from gpiozero import Button
from time import sleep
import sys

led = LED(17)
button = Button(2)

while True:
	button.wait_for_press()
	print('You asked for it smarty')
	led.toggle()

#while True:
#  led.on()
#  sleep(0.5)
#  led.off()
#  sleep(0.5)
