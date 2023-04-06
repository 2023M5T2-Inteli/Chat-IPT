# Importa bibliotecas necessárias
import pydobot
from serial.tools import list_ports
from pydobot.enums import PTPMode
from services.raspberry import Raspberry

# Define a classe Dobot
class Dobot:
    # Constructor a classe
    def __init__(self, _sio) -> None:
        self._cycle = 0  # Inicializa contador de ciclos
        self.maxCycles = 20  # Define o número máximo de ciclos
        self.magneticForce = 60000  # Define a força magnética
        self._stage = 0  # Inicializa a etapa atual
        self.pause = False  # Inicializa a variável de pausa
        self.sio = _sio  # Armazena a instância do Socket.IO
        self.raspberry_instance = Raspberry()  # Cria uma instância da classe Raspberry

        # Define a matriz de coordenadas para o movimento do braço robótico
        self.tray = [
            [
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": 10.1398, "y": -246.7926, "z": 102.9670, "r": -103.5851, "joint": True},
                {"x": -63.5785, "y": -295.5353, "z": -22.8625, "r": -101.3776, "joint": False},
                {"x": 91.9302, "y": -295.5699, "z": -22.8625, "r": -72.9041, "joint": False},
                {"x": -79.5393, "y": -268.1194, "z": -22.8625, "r": -103.1598, "joint": False},
                {"x": 96.3855, "y": -271.6446, "z": -34.8625, "r": -70.8550, "joint": False},
                {"x": -79.0650, "y": -208.2662, "z": -22.8625, "r": -110.3335, "joint": False},
                {"x": 99.2751, "y": -209.8143, "z": -22.8625, "r": -64.2235, "joint": False},
            ],

            [
                {"x": 10.1398, "y": -246.7926, "z": 102.9670, "r": -103.5851, "joint": True},
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -25.4011, "r": -22.4403, "joint": True},
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
            ],

            [
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
                {"x": 64.0797, "y": 269.9920, "z": -20.7218, "r": 67.5687, "joint": True},
                {"x": -70, "y": 269.9920, "z": -20.7218, "r": 67.5687, "joint": True},
                {"x": 64.0797, "y": 269.9920, "z": -20.7218, "r": 67.5687, "joint": True},
                {"x": -70, "y": 269.9920, "z": -20.7218, "r": 67.5687, "joint": True},
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
            ]
        ]

    # Retorna o ciclo atual
    @property
    def cycle(self):
        return self._cycle

    # Define um novo valor para o ciclo e emite o evento 'cycle' pelo Socket.IO
    @cycle.setter
    def cycle(self, novo_valor):
        self._cycle = novo_valor
        self.sio.emit('cycle', novo_valor + 1)
        self.sio.sleep(0)

    # Retorna a etapa atual
    @property
    def stage(self):
        return self._stage

    # Define um novo valor para a etapa e emite o evento 'stage' pelo Socket.IO
    @stage.setter
    def stage(self, novo_valor):
        self._stage = novo_valor
        self.sio.emit('stage', novo_valor + 1)
        self.sio.sleep(0)

    # Inicia a conexão com o dispositivo Dobot
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

    # Altera a bandeja com base nas últimas coordenadas fornecidas
    def change_tray(self, last_cords):
        try:
            while self.pause:
                self.sio.sleep(0)
                continue
            self.device._set_ptp_cmd(last_cords['x'],
                                     last_cords['y'],
                                     last_cords['z'],
                                     last_cords['r'],
                                     mode=PTPMode.MOVJ_XYZ,
                                     wait=True)
            self.sio.sleep(0)
        except Exception as err:
            print(err)

     # Realiza o movimento do braço robótico
    def movement(self) -> None:
        try:
            initial_stage = self.stage

            if self.stage == 2:
                self.raspberry_instance.send_command("0")
            else:
                self.raspberry_instance.send_command(str(self.magneticForce))

            for cords in self.tray[self.stage]:
                if self.stage != initial_stage:
                    (x, y, x, r, j1, j2, j3, j4) = self.device.pose()
                    self.change_tray({'x': x, 'y':  y, 'z': 151, 'r': r})
                    raise NameError("Stage changed!")
                while self.pause:
                    self.sio.sleep(0)
                    continue

                if cords['joint'] == True:
                    self.device._set_ptp_cmd(cords['x'],
                                             cords['y'],
                                             cords['z'],
                                             cords['r'],
                                             mode=PTPMode.MOVJ_XYZ,
                                             wait=True)
                else:
                    self.device.move_to(cords['x'],
                                        cords['y'],
                                        cords['z'],
                                        cords['r'],
                                        wait=True)
                self.sio.sleep(0)

            if (self.stage == 2):
                self.cycle += 1

            self.stage += 1
        except NameError as err:
            print(err)

    # Executa a parada de emergência do dispositivo Dobot
    def emergency_stop(self) -> bool:
        try:
            self.device.close()
            self.device = 0
            self.cycle = 0
            self.stage = 0

            self.sio.emit("response_emergency_stop",
                          "Emergency stop with success!")
            self.sio.sleep(5)

            return True
        except Exception as err:
            print(f"This error occuried: {err}")
            return False

