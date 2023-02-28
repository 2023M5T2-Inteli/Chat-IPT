from flask import Flask
from services.dobot import Dobot
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

dobot_instance = Dobot()


@app.route("/")
def home():
    return "Hello, world!"


@socketio.on('connect')
def handle_connect():
    response = dobot_instance.start_connection()
    if response:
        emit("resposta", "Dobot connected!")
    else:
        emit("error", {"from": "connect",
             "message": "Unable to connect with Dobot"})


@socketio.on('start_cicle')
def handle_start_cicle() -> None:
    cicle_count = 0
    emit("resposta", "Starting cicles")
    while cicle_count <= 20:
        emit("estagio", {"estagio": 1})
        dobot_instance.first_tray()
        emit("estagio", {"estagio": 2})
        dobot_instance.second_tray()
        emit("estagio", {"estagio": 3})
        dobot_instance.third_tray()
        cicle_count += 1
        emit("cicle", {"cicle": cicle_count})


@socketio.on('emergency_stop')
def handle_emergency_stop() -> None:
    response = dobot_instance.emergency_stop()
    if response:
        emit("resposta", "Dobot stoped!")
    else:
        emit("error", {"from": "emergency_stop",
             "message": "Dobot didn't stop"})


@socketio.on('disconnect_dobot')
def handle_disconnect_dobot() -> None:
    response = dobot_instance.end_connection()
    if response:
        emit("resposta", "Dobot disconnected!")
    else:
        emit("error", {"from": "disconnect_dobot",
             "message": "Dobot did not disconnected!"})


if __name__ == '__main__':
    socketio.run(app, port=3001)
