from flask import Flask, render_template
from services.dobot import Dobot
from flask_socketio import SocketIO, emit
import time

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*",
                    logger=True, engineio_logger=True)

dobot_instance = Dobot()


@app.route("/")
def home():
    return render_template('index.html')


@socketio.on('connect')
def handle_connect():
    response = dobot_instance.start_connection()
    if response:
        emit("resposta", "Dobot connected!")
    else:
        emit("error", {"from": "connect",
             "message": "Unable to connect with Dobot"})


@socketio.on('start_cycle')
def handle_start_cicle() -> None:
    cycle_count = 0
    emit("resposta", "Starting cycles")
    while dobot_instance.stage < 60:
        match dobot_instance.cycle:
            case 0:
                emit("stage", 1)
                dobot_instance.first_tray()
                dobot_instance.stage = 1
            case 1:
                emit("stage", 2)
                dobot_instance.second_tray()
                dobot_instance.stage = 2
            case 2:
                emit("stage", 3)
                dobot_instance.third_tray()
                dobot_instance.stage = 0
            case _:
                break
        dobot_instance.cycle += 1
        emit("cycle", cycle_count)
    dobot_instance.cycle = 0
    dobot_instance.stage = 0


@socketio.on('emergency_stop')
def handle_emergency_stop() -> None:
    response = dobot_instance.emergency_stop()
    if response:
        emit("resposta", "Dobot stoped!")
    else:
        emit("error", {"from": "emergency_stop",
             "message": "Dobot didn't stop"})

@socketio.on('advance_stage')
def handle_advance_stage() -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 1
        case 1:
            dobot_instance.stage = 2
        case 2:
            dobot_instance.stage = 0
        case _:
            emit("error", "Trying to reach an impossible stage")

@socketio.on('revert_stage')
def handle_revert_stage() -> None:
    match dobot_instance.stage:
        case 0:
            dobot_instance.stage = 2
        case 1:
            dobot_instance.stage = 0
        case 2:
            dobot_instance.stage = 1
        case _:
            emit("error", "Trying to reach an impossible stage")

@app.route('/disconnect_dobot')
def handle_disconnect_dobot():
    response = dobot_instance.end_connection()
    if response:
        emit("resposta", "Dobot disconnected!")
        dobot_instance.cycle = 0
        dobot_instance.stage = 0
        socketio.stop()
        return
    else:
        emit("error", "Dobot did not disconnected!")
    

if __name__ == '__main__':
    socketio.run(app, port=3001)