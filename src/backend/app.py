# Import the necessary libraries
import socketio
from services.dobot import Dobot
from services.raspberry import Raspberry
import socket
from eventlet import wsgi, listen
import PySimpleGUI as sg
import threading
import os
from engineio.async_drivers import gevent

# Server configuration
sio = socketio.Server(async_handlers=True, logger=True,
                      ping_interval=120, ping_timeout=120)
app = socketio.WSGIApp(sio)

dobot_instance = Dobot(sio)  # Create an instance of the Dobot object

# Function to get the server's IP address
def get_wifi_ip():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.connect(('10.255.255.255', 1))
            ip_address = s.getsockname()[0]
        except:
            ip_address = '127.0.0.1'
    return ip_address

# Socket connection event
@sio.event
def connect(sid, environ):
    print('Connected to socket')

# Dobot connection event
@sio.on('dobot_connect')
def dobot_connect(sid):
    response = dobot_instance.start_connection()
    if response:
        print("Robot connected!")
        sio.emit('response_dobot_connect')
    else:
        print('Error connecting to the robot')

# Event to start the cycle
@sio.on('start_cycle')
def handle_start_cicle(sid, arguments):
    print("Cycle starting")

    dobot_instance.maxCycles = arguments['cycles']
    dobot_instance.magneticForce = arguments['magneticForce']

    raspberry_instance = Raspberry()
    raspberry_instance.send_command(str(dobot_instance.magneticForce))

    while dobot_instance.cycle < dobot_instance.maxCycles:
        while dobot_instance.stage < 3:
            try:
                dobot_instance.movement()
            except Exception as err:
                print("Emergency button pressed!")
                return
        dobot_instance.stage = 0
    dobot_instance.emergency_stop()

# Stop event
@sio.on('stop')
def stop(sid):
    dobot_instance.pause = True
    sio.emit("response_stop")
    sio.sleep(0)

# Reactivate event
@sio.on('reactivate')
def reactivate(sid):
    sio.emit("response_reactivate")
    sio.sleep(0)
    dobot_instance.pause = False

# Emergency stop event
@sio.on('emergency_stop')
def handle_emergency_stop(sid) -> None:
    print("Emergency stop triggered!")
    dobot_instance.emergency_stop()

# Tray advance event
@sio.on('advance_stage')
def handle_advance_stage(sid) -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 1
        case 1:
            dobot_instance.stage = 2
        case 2:
            dobot_instance.stage = 0
            dobot_instance.cycle += 1
        case _:
            print('error: ')
    sio.emit("response_advance_stage")

# Event to go to the previous tray
@sio.on('previous_stage')
def handle_advance_stage(sid) -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 2
            dobot_instance.cycle -= 1
        case 1:
            dobot_instance.stage = 0
        case 2:
            dobot_instance.stage = 1

        case _:
            print('error: ')
    sio.emit("response_previous_stage")

# Socket disconnection event
@sio.event
def disconnect(sid):
    print('Disconnected from socket')
    raspberry_instance = Raspberry()
    raspberry_instance.send_command("0")
    dobot_instance.emergency_stop()

# Function to start the server
def start_server():
    ip = get_wifi_ip()
    wsgi.server(listen((str(ip), 3001)), app)


# Get IP to display in the popup
ip = get_wifi_ip()

# Create the popup layout
sg.theme("DarkBlack")

column_to_be_centered = [[sg.Text('Servidor rodando com sucesso!', font=('Times New Roman', 16))],
                         [sg.Text("Por favor, insira os seguintes números em seu aplicativo:", font=(
                             'Times New Roman', 16))],
                         [sg.Text(str(ip), font=(
                             'Times New Roman', 20, 'bold'))],
                         [sg.Text('Caso deseja encerrar o servidor Flask, pressione o botão abaixo.', font=(
                             'Times New Roman', 16))],
                         [sg.Button('ENCERRAR', font=('Times New Roman', 16), button_color=())]]

layout = [[sg.VPush()],
          [sg.Push(), sg.Column(column_to_be_centered,
                                element_justification='c'), sg.Push()],
          [sg.VPush()]]

# Create the popup window
window = sg.Window('Chat IPT', layout, size=(500, 300))

# Run when the script is the main file
if __name__ == '__main__':
    # Start the Flask server in a separate thread
    flask_thread = threading.Thread(target=start_server)
    flask_thread.start()
    # Loop in case the popup button is pressed to close the server
    while True:
        event, values = window.read()
        if event == 'ENCERRAR':
            os._exit(0)
