import sys
from machine import Pin, PWM
from time import sleep
try:
    import usocket as socket
except:
    import socket

import network

# Setting PWN pinout and frequence
pwm = PWM(Pin(0))
pwm.freq(1000)
from machine import Pin
# Function to turn on the PWM so then the electromagnetic magnet will turn on
# Max value for the PWM is 65_000


def turn_on_PWM(value: int) -> bool:
    try:
        pwm.duty_u16(value)
        return True
    except:
        return False

# Function to turn off(fixed value of 0) the PWM so then the electromagnetic magnet will turn on


def turn_off_PWM() -> bool:
    try:
        pwm.duty_u16(0)
        return True
    except:
        return False


# Loop of execution
if __name__ == "__main__":
    station = network.WLAN(network.AP_IF)
    station.config(ssid="Chat Ipt", key="12345678")
    station.active(True)

    led = Pin("LED", Pin.OUT)
    led.on()
    
    while True:
        try:
            
            # Will read any information that was passed throught the standar pin of the raspberry pi pico w.
            call = sys.stdin.readline().strip()

            # Cases that raspberry pi will perform some activity.
            # If we pass 0, that means we want to turn off the PWM.
            if int(call) == 0:
                turn_off_PWM()

            # If we pass any value diferent from zero and less then the max value of PWM, it will turn on the electromagnetic magnet with that value.
            elif int(call) > 0 and int(call) <= 65000:
                turn_on_PWM(int(call))

        except:
            # Some activity so then the rapsberry wont watchdog.
            sleep(0.4)
            pass
