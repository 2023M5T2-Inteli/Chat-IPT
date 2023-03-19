import socketio
import asyncio
from services.dobot import Dobot
from aiohttp import web
import eventlet

sio = socketio.Server(async_handlers=True, logger=True, ping_interval=120, ping_timeout=120)
app = socketio.WSGIApp(sio)

dobot_instance = Dobot(sio)

@sio.event
def connect(sid, environ):
    print('Conectado ao socket')

@sio.on('dobot_connect')
def dobot_connect(sid):
    response = dobot_instance.start_connection()
    if response:
        print("Robô conectado!")
        sio.emit('response_dobot_connect')
    else:
        print('Erro ao conectar com o robô')

@sio.on('start_cycle')
def handle_start_cicle(sid):
    print("Ciclo começando")

    while dobot_instance.cycle < 20:
        while dobot_instance.stage < 3:
            if dobot_instance.stage == 0:
                dobot_instance.first_tray(socketio=socketio)
            elif dobot_instance.stage == 1:
                dobot_instance.second_tray(socketio=socketio)
            elif dobot_instance.stage == 2:
                dobot_instance.third_tray(socketio=socketio)
        dobot_instance.stage = 0
    
@sio.on('stop')
def stop(sid):
    dobot_instance.pause = True
    sio.emit("response_stop")
    sio.sleep(0)

@sio.on('reactivate')
def reactivate(sid):
    sio.emit("response_reactivate")
    sio.sleep(0)
    dobot_instance.pause = False

@sio.on('emergency_stop')
def handle_emergency_stop(sid) -> None:
    print("Parada de emergência acionada!")
    dobot_instance.emergency_stop()

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
    
@sio.event
def disconnect(sid):
    print('Disconectado ao socket')
    dobot_instance.emergency_stop()

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('127.0.0.1', 3001)), app)
