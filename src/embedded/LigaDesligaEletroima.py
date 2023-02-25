from machine import Pin
from time import sleep

#Pino Ponte H
eletro_ima = Pin(0, Pin.OUT)

#Condição abaixo liga e desliga o eletroíma a cada 1s. 
while True:
    eletro_ima.value(0)
    sleep(1)
    eletro_ima.value(1)
    sleep(1)

