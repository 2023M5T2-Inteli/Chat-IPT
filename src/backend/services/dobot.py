# Import necessary libraries
import pydobot
from serial.tools import list_ports
from pydobot.enums import PTPMode
from services.raspberry import Raspberry

# Define the Dobot class
class Dobot:
    # Constructor of the class
    def __init__(self, _sio) -> None:
        self._cycle = 0  # Initialize cycle counter
        self.maxCycles = 20  # Set the maximum number of cycles
        self.magneticForce = 60000  # Set the magnetic force
        self._stage = 0  # Initialize the current stage
        self.pause = False  # Initialize the pause variable
        self.sio = _sio  # Store the Socket.IO instance

        # Define the coordinate matrix for the robotic arm movement
        self.tray = [
            [
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": 0, "y": -235, "z": 151, "r": -89, "joint": True},
                {"x": 93, "y": -282, "z": -10, "r": -71, "joint": False},
                {"x": -61, "y": -288, "z": -10, "r": -101, "joint": False},
                {"x": 88, "y": -258, "z": -10, "r": -70, "joint": False},
                {"x": -60, "y": -253, "z": -10, "r": -103, "joint": False},
                {"x": 88, "y": -229, "z": -10, "r": -68, "joint": False},
                {"x": -63, "y": -236, "z": -10, "r": -104, "joint": False},
                # {"x": 99.2751, "y": -209.8143, "z": -25, "r": -64.2235, "joint": False},
            ],

            [
                {"x": 10.1398, "y": -246.7926, "z": 102.9670, "r": -103.5851, "joint": True},
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -10, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -10, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -10, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -10, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": -47.6883, "z": -10, "r": -22.4403, "joint": True},
                {"x": 200.7883, "y": 80, "z": -10, "r": -22.4403, "joint": True},
                {"x": 228, "y": 0, "z": 151, "r": 0, "joint": True},
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
            ],

            [
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
                {"x": 64.0797, "y": 269.9920, "z": -10, "r": 67.5687, "joint": True},
                {"x": -70, "y": 269.9920, "z": -10, "r": 67.5687, "joint": True},
                {"x": 64.0797, "y": 269.9920, "z": -10, "r": 67.5687, "joint": True},
                {"x": -70, "y": 269.9920, "z": -10, "r": 67.5687, "joint": True},
                {"x": -7.2212, "y": 234.4742, "z": 123.2508, "r": 82.6842, "joint": True},
            ]
        ]

    @property
    def cycle(self):
        return self._cycle

    # Set a new value for the cycle and emit the 'cycle' event through Socket.IO
    @cycle.setter
    def cycle(self, new_value):
        self._cycle = new_value
        self.sio.emit('cycle', new_value + 1)
        self.sio.sleep(0)

    # Return the current stage
    @property
    def stage(self):
        return self._stage

    # Set a new value for the stage and emit the 'stage' event through Socket.IO
    @stage.setter
    def stage(self, new_value):
        self._stage = new_value
        self.sio.emit('stage', new_value + 1)
        self.sio.sleep(0)

    # Start the connection with the Dobot device
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

    # Change the tray based on the last provided coordinates
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

     # Perform the robotic arm movement
    def movement(self) -> None:
        try:
            initial_stage = self.stage

            if self.stage == 2:
                raspberry_instance = Raspberry()
                raspberry_instance.send_command("0")
            else:
                raspberry_instance = Raspberry()
                raspberry_instance.send_command(str(self.magneticForce))

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

            self.sio.sleep(0.5)
            if self.stage != initial_stage:
                (x, y, x, r, j1, j2, j3, j4) = self.device.pose()
                self.change_tray({'x': x, 'y':  y, 'z': 151, 'r': r})
                raise NameError("Stage changed!")
            self.stage += 1
        except NameError as err:
            print(err)

    # Execute the emergency stop of the Dobot device
    def emergency_stop(self) -> bool:
        try:
            self.device.close()
            self.device = 0
            self.cycle = 0
            self.stage = 0

            raspberry_instance = Raspberry()
            raspberry_instance.send_command("0")

            self.sio.emit("response_emergency_stop",
                          "Emergency stop with success!")
            self.sio.sleep(5)

            return True
        except Exception as err:
            print(f"This error occurred: {err}")
            return False
