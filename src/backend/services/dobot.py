import pydobot
from serial.tools import list_ports

class Dobot:
    def __init__(self, _sio) -> None:
        self._cycle = 0
        self._stage = 0
        self.pause = False
        self.sio = _sio
        self.tray = [[{"x": 228,"y": 0,"z": 151,"r": 0}, {"x": 203, "y": -283, "z": 109, "r": -53}, {"x": -94, "y": -333, "z": 85, "r": -105}, {"x": 112, "y": -331, "z": 75, "r": -71}, {"x": 112, "y": -254, "z": 82,"r":-65}, {"x": -96, "y": -261, "z": 80, "r": -110}, {"x": -96, "y": -198, "z": 90, "r":-115}, {"x": 113, "y": -212, "z": 87, "r": -61}, {"x": 203, "y": -283, "z": 109, "r": -53}], [{"x": 228,"y": 0,"z": 151,"r": 0}, {"x": 237, "y": -70, "z": 28, "r": - 16}, {"x": 235, "y": 88, "z": 24, "r": 21}, {"x": 237, "y": -70, "z": 28, "r": -16}, {"x": 235, "y": 88, "z": 24, "r": 21}, {"x": 237, "y": -70, "z": 28, "r": -16}, {"x": 235, "y": 88, "z": 24, "r": 21}], [{"x": 228,"y": 0,"z": 151,"r": 0}, {"x":211, "y": 224, "z": 86, "r": 46}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 211, "y": 224, "z": 86, "r": 46}]]

    @property
    def cycle(self):
        return self._cycle
    
    @cycle.setter
    def cycle(self, novo_valor):
        self._cycle = novo_valor
        self.sio.emit('cycle', novo_valor + 1)
        self.sio.sleep(0)

    @property
    def stage(self):
        return self._stage
    
    @stage.setter
    def stage(self, novo_valor):
        self._stage = novo_valor
        self.sio.emit('stage', novo_valor + 1)
        self.sio.sleep(0)

    def start_connection(self) -> bool:
        available_ports = list_ports.comports()
        for port in available_ports:
            try:
                device = pydobot.Dobot(port=port.device, verbose=False)
                self.device = device
                return True
            except:
                print(
                    f"Wrong port: {port.device}, trying another one...")
                continue
        return False

    def first_tray(self, socketio) -> None:
        try:
            for cords in self.tray[0]:
                if self.stage != 0:
                    raise Exception("Stage changed!")
                while self.pause:
                    self.sio.sleep(0)
                    continue
                self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)
                self.sio.sleep(0)
            self.stage =1
        except Exception as err:
            print(err)

    def second_tray(self, socketio) -> None:
        try:
            for cords in self.tray[1]:
                if self.stage != 1:
                    raise Exception("Stage changed!")
                while self.pause:
                    self.sio.sleep(0)
                    continue
                self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)
                self.sio.sleep(0)
            self.stage = 2

        except Exception as err:
            print(err)

    def third_tray(self, socketio) -> None:
        try:
            for cords in self.tray[2]:
                if self.stage != 2:
                    raise Exception("Stage changed!")
                while self.pause:
                    self.sio.sleep(0)
                    continue
                self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)
                self.sio.sleep(0)
            self.stage += 1
            self.cycle += 1

        except Exception as err:
            print(err)

    def emergency_stop(self) -> bool:
        try:
            self.device.close()

            self.sio.emit("response_emergency_stop", "Emergency stop with success!")
            self.sio.sleep(5)

            return True
        except Exception as err:
            print(f"This error occuried: {err}")
            return False