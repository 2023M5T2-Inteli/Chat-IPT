import network
import socket
from time import sleep
from machine import Pin, PWM
import json

pwm = PWM(Pin(0))
pwm.freq(1000)

ssid = 'Galaxy A53 5G'
password = 'qhvz8247'
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip

def open_socket(ip):
    # Open a socket
    address = (ip, 81)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection


def serve(connection):
    #Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        try:
            request = str(request, 'utf8')
            json_string = ''
            control = -100
            for i in range(len(request) - 1):
                if request[i] == '{':
                    json_string += request[i]
                    control = 1
                    while request[i + control] != '}':
                        json_string += request[i + control]
                        control += 1
                pass
            json_string += '}'
            obj = json.loads(json_string)
            print(obj['PWM_value'])
            pwm.duty_u16(obj['PWM_value'])
        except Exception as err:
            print(err)
        
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n {"code": "SUCCESS"}')
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()

