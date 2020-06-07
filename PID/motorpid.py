import RPi.GPIO as gpio
from time import sleep

gpio.setmode(gpio.BOARD)

gpio.setup(40, gpio.OUT)
pwm_obj=gpio.PWM(40,1000)

pwm_obj.start(0)  #duty cycle on time/total time

for i in range(0,101,5):
	pwm_obj.ChangeDutyCycle(i)
	sleep(0.3)

for i in range(100,1,-5):
	pwm_obj.ChangeDutyCycle(i)
	sleep(0.3)

