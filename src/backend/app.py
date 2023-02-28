from flask import Flask, render_template
from services.dobot import Dobot
from flask_socketio import SocketIO, emit
import time

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
    cicle_count = 0
    emit("resposta", "Starting cycles")
    while cicle_count <= 20:
        emit("stage", {"estagio": 1})
        # dobot_instance.first_tray()
        emit("stage", {"estagio": 2})
        # dobot_instance.second_tray()
        emit("stage", {"estagio": 3})
        # dobot_instance.third_tray()
        cicle_count += 1
        emit("cycle", {"cicle": cicle_count})
        time.sleep(5)


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
