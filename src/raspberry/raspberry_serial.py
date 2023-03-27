import sys
from machine import Pin, PWM
from time import sleep
from hx711 import HX711

# Setting the
driver = HX711(d_out=5, pd_sck=4)

# Setting PWN pinout and frequence
pwm = PWM(Pin(0))
pwm.freq(1000)

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

# Function to read the value that the scale is capturing at the moment


def read_balanca() -> int:
    return driver.read()


# Loop of execution
if __name__ == "__main__":
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

            # If we pass the keyword "balanca", that means we want that the raspberry pi send us what the scale is reading at that moment. So then, the raspberry pi will format the value and send through the device's standard out that information.
            elif call.lower() == "balanca":
                data = str(read_balanca())
                sys.stdout.write(bytes(data.encode()) + b"\n")

        except:
            # Some activity so then the rapsberry wont watchdog.
            sleep(0.4)
            pass
