import ujson
from network import WLAN
import microdot
import urequests
import utime
from machine import Pin, PWM

#Tamanho da largura do pulso do sinal PWM
# PWM_width = 0
# 
# #Pino da ponte H
# pwm = PWM(Pin(0))
# 
# #Frequência sinal PWM
# pwm.freq(1000)
# 
# #Deserializando json
# parsedJson = ujson.loads("""{"device":"electromagnetic", "value":50123}""")
# 
# print (parsedJson["device"])
# print (parsedJson["value"])
#  
# gauss = parsedJson["value"]
# print(gauss)

# pwm.duty_u16(gauss)

WLAN.connect('Galaxy A53 5G', 'qhvz8247')

while not wlan.isconnected() and wlan.status() >= 0:
 print("Waiting to connect:")
 time.sleep(0.5)

app = Microdot()

@app.route('/')
def index():
    print("Funcionou!")
    return "OK!"

WLAN.ifconfig()
app.run(port=80)




# response = urequests.post("http://jsonplaceholder.typicode.com/posts", data = "some dummy content")






































#Rampa que varia o sinal de PWM de 0 até o máximo 65536
# #Quando o valor é menor que o máximo, o pulso recebe += para aumentar a intensidade da força magnética atual em 10 em intervalo de 1ms
# while True:  
#     while PWM_width < 65536:
#         PWM_width += 10
#         utime.sleep(0.001)
#         pwm.duty_u16(gauss)
#         print (gauss)
#       
# # #Quando o valor é maior que 0, o pulso recebe -= para diminuir a intensidade da força magnética atual em 10 em intervalo de 1ms      
#     while PWM_width > 0:
#         PWM_width -= 10
#         utime.sleep(0.001)
#         pwm.duty_u16(gauss)
#         print (gauss)




