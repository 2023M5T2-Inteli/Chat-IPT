import utime
from machine import Pin, PWM

#Tamanho da largura do pulso do sinal PWM
PWM_width = 0

#Pino da ponte H
pwm = PWM(Pin(0))

#Frequência sinal PWM
pwm.freq(1000)

#Rampa que varia o sinal de PWM de 0 até o máximo 65536
#Quando o valor é menor que o máximo, o pulso recebe += para aumentar a intensidade da força magnética atual em 10 em intervalo de 1ms
while True:  
  while PWM_width < 65536:
      PWM_width += 10
      utime.sleep(0.001)
      pwm.duty_u16(PWM_width)
      print (PWM_width)
      
#Quando o valor é maior que 0, o pulso recebe -= para diminuir a intensidade da força magnética atual em 10 em intervalo de 1ms      
  while PWM_width > 0:
      PWM_width -= 10
      utime.sleep(0.001)
      pwm.duty_u16(PWM_width)
      print (PWM_width)
