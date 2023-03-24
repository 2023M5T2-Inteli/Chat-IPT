import sys
from machine import Pin, PWM
from time import sleep
from hx711 import HX711

# Setting the 
driver = HX711(d_out=5, pd_sck=4)

# Setting PWN pinout and frequence
pwm = PWM(Pin(0))
pwm.freq(1000)

def turn_on_PWM(value: int) -> bool:
   try:
      pwm.duty_u16(value)
      return True
   except:
      return False

def turn_off_PWM() -> bool:
   try:
      pwm.duty_u16(0)
      return True
   except:
      return False
   
def read_balanca() -> int:
   return driver.read()

# Loop of execution
if __name__ == "__main__":
   while True:
      try:
         # Realiza uma leitura de informação da serial
         call = sys.stdin.readline().strip()

         if int(call) == 0:
            turn_off_PWM()

         elif int(call) > 0 and int(call) <= 65000 :
            turn_on_PWM(int(call))
         
         elif call.lower() == "balanca":
            data = str(read_balanca())
            sys.stdout.write(bytes(data.encode()) + b"\n")
      
      except:
         sleep(0.4)
         pass