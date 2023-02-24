#código para distância
from machine import Pin, I2C
import utime
#marcação dos GPIO
trigger = Pin(17,Pin.OUT)
echo = Pin(16, Pin.IN)
#marcação inicial
distancia = 0


i2c = I2C(0,sda=Pin(0), scl=Pin(1),freq=40000)

while True:
    trigger.high()
    utime.sleep(1)
    trigger.low()
    
    while echo.value() == 0:
        comienzo = utime.ticks_us()
    while echo.value() == 1:
        final = utime.ticks_us()
    
    duracion = final - comienzo
    distancia = (duracion * 0.0343) / 2
    print("Distancia:",distancia,"cm")
    
    utime.sleep(0.5)