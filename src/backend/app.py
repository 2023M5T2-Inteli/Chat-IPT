from flask import Flask, render_template
from services.dobot import Dobot
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

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
                try:
                    emit("stage", 1)
                    dobot_instance.first_tray()
                    dobot_instance.cycle = 1
                except:
                    return
            case 1:
                try:
                    emit("stage", 2)
                    dobot_instance.second_tray()
                    dobot_instance.cycle = 2
                except:
                    return
            case 2:
                try:
                    emit("stage", 3)
                    dobot_instance.third_tray()
                    dobot_instance.cycle = 0
                except:
                    return
            case _:
                break
        dobot_instance.stage += 1
        emit("cycle", cycle_count)
    dobot_instance.cycle = 0
    dobot_instance.stage = 0


@socketio.on('stop')
def handle_stop() -> None:
    dobot_instance.pause = True
    while dobot_instance.pause == True:
        response = dobot_instance.stop()
        if response:
            emit("resposta", "Dobot stoped!")
        else:
            emit("error", {"from": "stop", "message": "Dobot did not stop"})


@socketio.on('reactivate')
def handle_reactivate() -> None:
    dobot_instance.pause = False

    if dobot_instance.pause == False:
        emit("resposta", "Dobot activated!")
    else:
        emit("error", {"from": "reactivate",
             "message": "Dobot did not reactivate"})


@socketio.on('emergency_stop')
def handle_emergency_stop() -> None:
    response = dobot_instance.emergency_stop()
    print(response)
    if response:
        emit("resposta", "Emergency stop with success!")
    else:
        emit("error", {"from": "emergency_stop",
             "message": "Emergency stop did not finished with success"})


@socketio.on('advance_stage')
def handle_advance_stage() -> None:
    match dobot_instance.cycle:
        case 0:
            dobot_instance.cycle = 1
        case 1:
            dobot_instance.cycle = 2
        case 2:
            dobot_instance.cycle = 0
        case _:
            emit("error", "Trying to reach an impossible stage")
    dobot_instance.stage += 1
    (x, y, z, r, j1, j2, j3, j4) = dobot_instance.device.pose()
    dobot_instance.device.move_to(x, y, 151, r)
    dobot_instance.device.move_to(228, y, 151, r)


@socketio.on('revert_stage')
def handle_revert_stage() -> None:
    match dobot_instance.cycle:
        case 0:
            dobot_instance.cycle = 2
        case 1:
            dobot_instance.cycle = 0
        case 2:
            dobot_instance.cycle = 1
        case _:
            emit("error", "Trying to reach an impossible stage")
    dobot_instance.stage -= 1
    (x, y, z, r, j1, j2, j3, j4) = dobot_instance.device.pose()
    dobot_instance.device.move_to(x, y, 151, r)
    dobot_instance.device.move_to(228, y, 151, r)


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
    socketio.run(app, host='0.0.0.0', port=3001, debug=True)
