import pydobot
from serial.tools import list_ports


class Dobot:

    def __init__(self) -> None:
        self.cycle = 0
        self.stage = 0
        self.pause = False
        self.tray = [[{"x": 228,"y": 0,"z": 151,"r": 0}, {"x": 203, "y": -283, "z": 109, "r": -53}, {"x": -94, "y": -333, "z": 85, "r": -105}, {"x": 112, "y": -331, "z": 75, "r": -71}, {"x": 112, "y": -254, "z": 82,"r":-65}, {"x": -96, "y": -261, "z": 80, "r": -110}, {"x": -96, "y": -198, "z": 90, "r":-115}, {"x": 113, "y": -212, "z": 87, "r": -61}, {"x": 203, "y": -283, "z": 109, "r": -53}], [{"x": 228,"y": 0,"z": 151,"r": 0}, {"x": 237, "y": -70, "z": 28, "r": - 16}, {"x": 235, "y": 88, "z": 24, "r": 21}, {"x": 237, "y": -70, "z": 28, "r": -16}, {"x": 235, "y": 88, "z": 24, "r": 21}, {"x": 237, "y": -70, "z": 28, "r": -16}, {"x": 235, "y": 88, "z": 24, "r": 21}], [{"x": 228,"y": 0,"z": 151,"r": 0}, {"x":211, "y": 224, "z": 86, "r": 46}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 114, "y": 250, "z": 20, "r": 65}, {"x": -29, "y": 256, "z": 20, "r": 96}, {"x": 211, "y": 224, "z": 86, "r": 46}]]

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

    def end_connection(self) -> bool:
        try:
            self.device.close()
            self.start_connection()
            self.device.move_to(228, 0, 151, 0, wait=True)
            self.device.close()
            return True
        except:
            print("Device unable to desconnected!")
            return False

    def first_tray(self) -> None:

        # self.device.move_to(203, -283,
        #                     109, -53, wait=True)
        # self.device.move_to(-94, -333,
        #                     85, -105, wait=True)
        # self.device.move_to(112, -331,
        #                     75, -71, wait=True)
        # self.device.move_to(112, -254,
        #                     82, -65, wait=True)
        # self.device.move_to(-96, -261,
        #                     80, -110, wait=True)
        # self.device.move_to(-96, -198,
        #                     90, -115, wait=True)
        # self.device.move_to(113, -212,
        #                     87, -61, wait=True)
        # self.device.move_to(203, -283,
        #                     109, -53, wait=True)
        for cords in self.tray[0]:
            if self.cycle != 0:
                raise Exception("Stage changed!")
            while self.pause:
                continue
            self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)

    def second_tray(self) -> None:

        # self.device.move_to(237, -70, 28, -16, wait=True)
        # self.device.move_to(235, 88, 24, 21, wait=True)
        # self.device.move_to(237, -70, 28, -16, wait=True)
        # self.device.move_to(235, 88, 24, 21, wait=True)
        # self.device.move_to(237, -70, 28, -16, wait=True)
        # self.device.move_to(235, 88, 24, 21, wait=True)

        for cords in self.tray[1]:
            if self.cycle != 1:
                raise Exception("Stage changed!")
            while self.pause:
                continue
            self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)

    def third_tray(self) -> None:

        # self.device.move_to(211, 224, 86, 46, wait=True)
        # self.device.move_to(114, 250, 20, 65, wait=True)
        # self.device.move_to(-29, 256, 20, 96, wait=True)
        # self.device.move_to(114, 250, 20, 65, wait=True)
        # self.device.move_to(-29, 256, 20, 96, wait=True)
        # self.device.move_to(114, 250, 20, 65, wait=True)
        # self.device.move_to(-29, 256, 20, 96, wait=True)

        # self.device.move_to(211, 224, 86, 46, wait=True)

        for cords in self.tray[2]:
            if self.cycle != 2:
                raise Exception("Stage changed!")
            while self.pause:
                continue
            self.device.move_to(cords['x'], cords['y'], cords['z'], cords['r'], wait=True)

    def stop(self) -> bool:
        try:
            self.device.wait(500)
            # self.start_connection()
            return True
        except Exception as err:
            print(f"This error occuried: {err}")
            return False

    def emergency_stop(self) -> bool:
        try:
            self.device.close()
            self.start_connection()
            (x, y, z, r, j1, j2, j3, j4) = self.device.pose()
            # self.device.move_to(228, 0, 151, 0, wait=True)
            self.device.move_to(x, y, 151, r, wait=True)
            return True
        except Exception as err:
            print(f"This error occuried: {err}")
            return False
