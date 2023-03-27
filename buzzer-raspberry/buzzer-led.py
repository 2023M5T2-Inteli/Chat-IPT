#após algum erro de rotação será acionado
#um buzzer e um led acederá.

from machine import Pin, PWM
from time import sleep
from utime import sleep

led = Pin(16, Pin.OUT)
while True:
    led.high()
    sleep(1)
    led.low() 
    sleep(1)

buzzer = PWM(Pin(16))

buzzer.freq(1000)

buzzer.duty_u16(100000)

sleep(0.5)
buzzer.duty_u16(0)




