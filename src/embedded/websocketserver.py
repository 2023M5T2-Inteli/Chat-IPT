# ujson.loads("""{"device":"electromagnetic", "value":50123}""")
#         client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')



import network
import socket
from time import sleep
import machine
import ujson

ssid = 'Galaxy A53 5G'
password = 'qhvz8247'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
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
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    #Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        response = 'Hello!'
        client.send(response)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()



# import network
# import socket
# from time import sleep
# import machine
# import ujson

# ssid = 'Galaxy A53 5G'
# password = 'qhvz8247'

# def connect():
#     #Connect to WLAN
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(ssid, password)
    
# def connect():
#     #Connect to WLAN
#     wlan = network.WLAN(network.STA_IF)
#     wlan.active(True)
#     wlan.connect(ssid, password)
#     while wlan.isconnected() == False:
#         print('Waiting for connection...')
#         sleep(1)
#     ip = wlan.ifconfig()[0]
#     print(f'Connected on {ip}')
#     return ip

# def open_socket(ip):
#     # Open a socket
#     address = (ip, 80)
#     connection = socket.socket()
#     connection.bind(address)
#     connection.listen(1)
#     return connection

# def serve(connection):
#     #Start a web server
#     while True:
#         client = connection.accept()[0]
#         request = client.recv(1024)
#         request = str(request)
#         print(request)
#         response = ujson.loads("""{"device":"electromagnetic", "value":50123}""")
#         client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
#         client.send(response)
#         client.close()

# try:
#     ip = connect()
#     connection = open_socket(ip)
#     serve(connection)
# except KeyboardInterrupt:
#     machine.reset()





#---------------------
import network
import socket
from time import sleep
import machine
import ujson

ssid = 'Galaxy A53 5G'
password = 'qhvz8247'

def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    
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
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    #Start a web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)
        response = ujson.loads("""{"device":"electromagnetic", "value":50123}""")
        client.send('HTTP/1.0 200 OK\r\nContent-type: application/json\r\n\r\n')
        client.send(response)
        client.close()

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()
