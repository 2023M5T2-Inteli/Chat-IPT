from flask import Flask, render_template, make_response, jsonify
from services.dobot import Dobot
from flask_socketio import SocketIO, emit
import requests
import asyncio

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*", ping_timeout=240, ping_interval=5)

dobot_instance = Dobot()

# @app.route("/")
# def home():
#     return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    emit("response_connect", "Socket connected!")
    

@socketio.on('dobot_connect')
def handle_connect():
    response = dobot_instance.start_connection()
    if response:
        print("Robô conectado!")
        emit("response_dobot_connect", "Dobot connected!")
    else:
        emit("error", {"from": "connect",
             "message": "Unable to connect with Dobot"})
        

async def dobot_movement():
    print("Comecando o movimentoo")
    print(dobot_instance)
    while dobot_instance.cycle < 20:
        while dobot_instance.stage < 3:
            if dobot_instance.stage == 0:
                emit("stage", 1)
                socketio.sleep(0)
                dobot_instance.first_tray(socketio=socketio)
            elif dobot_instance.stage == 1:
                emit("stage", 2)
                socketio.sleep(0)
                dobot_instance.second_tray(socketio=socketio)
            elif dobot_instance.stage == 2:
                emit("stage", 3)
                socketio.sleep(0)
                dobot_instance.third_tray(socketio=socketio)
            dobot_instance.stage += 1
        dobot_instance.stage = 0
        dobot_instance.cycle += 1
        emit("cycle", dobot_instance.cycle + 1)
        socketio.sleep(0)

@socketio.on('start_cycle')
def handle_start_cicle() -> None:
    print("Ciclo começando")

    try:
        asyncio.run(dobot_movement())
        
    except Exception as err :
        print(err)
        return
    
@socketio.on("teste")
def teste() -> None:
    print("teste de socket foi")


@socketio.on('stop')
def handle_stop() -> None:
    print("stop")
    dobot_instance.pause = True
    while dobot_instance.pause == True:
        response = dobot_instance.stop()
        # if response:
        #     emit("response_stop", "Dobot stoped!")
        #     socketio.sleep(0)
        # else:
        #     emit("error", {"from": "stop", "message": "Dobot did not stop"})

@socketio.on('reactivate')
def handle_reactivate() -> None:
    dobot_instance.pause = False

    if dobot_instance.pause == False:
        emit("response_reactivate", "Dobot activated!")
    else:
        emit("error", {"from": "reactivate",
             "message": "Dobot did not reactivate"})


@socketio.on('emergency_stop')
def handle_emergency_stop() -> None:
    print("Parada de emergência acionada!")
    response = dobot_instance.emergency_stop()
    
    if response:
        emit("response_emergency_stop", "Emergency stop with success!")
    else:
        emit("error", {"from": "emergency_stop",
             "message": "Emergency stop did not finished with success"})


@socketio.on('advance_stage')
def handle_advance_stage() -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 1
        case 1:
            dobot_instance.stage = 2
        case 2:
            dobot_instance.stage = 0
            dobot_instance.cycle += 1

        case _:
            emit("error", "Trying to reach an impossible stage")
    dobot_instance.cycle += 1
    (x, y, z, r, j1, j2, j3, j4) = dobot_instance.device.pose()
    dobot_instance.device.move_to(x, y, 151, r)
    dobot_instance.device.move_to(228, y, 151, r)
    emit("response_advance_stage", "Advanced stage with success!")


@socketio.on('revert_stage')
def handle_revert_stage() -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 2
            dobot_instance.cycle -= 1
        case 1:
            dobot_instance.stage = 0
        case 2:
            dobot_instance.stage = 1
        case _:
            emit("error", "Trying to reach an impossible stage")
    
    (x, y, z, r, j1, j2, j3, j4) = dobot_instance.device.pose()
    dobot_instance.device.move_to(x, y, 151, r)
    dobot_instance.device.move_to(228, y, 151, r)
    emit("response_revert_stage", "Reverted stage with success!")


@app.route('/disconnect_dobot')
def handle_disconnect_dobot():
    response = dobot_instance.end_connection()
    if response:
        dobot_instance.stage = 0
        dobot_instance.stage = 0
        socketio.stop()
        resposta = {'code': 'SUCCESS', 'message': 'Dobot disconnect with success!'}
        return make_response(jsonify(resposta), 200)
    else:
        emit("error", "Dobot did not disconnected!")


if __name__ == '__main__':
    socketio.run(app, port=3001, debug=True)
# host="192.168.197.134",