#from machine import freq
#freq(160000000)
from hx711 import HX711
from time import sleep
driver = HX711(d_out=5, pd_sck=4)
while True:
	data = driver.read()
	print("Dado Lido:", data)
	sleep(2)
#driver.channel=HX711.CHANNEL_A_64
#data = driver.read()
#print("Dado Lido:", data)