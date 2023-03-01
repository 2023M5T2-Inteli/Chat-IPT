import pydobot
from serial.tools import list_ports


class Dobot:

    def __init__(self) -> None:
        self.cycle = 0
        self.stage = 0

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
            self.device.move_to(228, 0, 151, 0, wait=True)
            self.device.close()
            return True
        except:
            print("Device unable to desconnected!")
            return False

    def first_tray(self) -> None:

        self.device.move_to(203, -283,
                            109, -53, wait=True)
        self.device.move_to(-94, -333,
                            85, -105, wait=True)
        self.device.move_to(112, -331,
                            75, -71, wait=True)
        self.device.move_to(112, -254,
                            82, -65, wait=True)
        self.device.move_to(-96, -261,
                            80, -110, wait=True)
        self.device.move_to(-96, -198,
                            90, -115, wait=True)
        self.device.move_to(113, -212,
                            87, -61, wait=True)
        self.device.move_to(203, -283,
                            109, -53, wait=True)

    def second_tray(self) -> None:

        self.device.move_to(237, -70, 28, -16, wait=True)
        self.device.move_to(235, 88, 24, 21, wait=True)
        self.device.move_to(237, -70, 28, -16, wait=True)
        self.device.move_to(235, 88, 24, 21, wait=True)
        self.device.move_to(237, -70, 28, -16, wait=True)
        self.device.move_to(235, 88, 24, 21, wait=True)

    def third_tray(self) -> None:

        self.device.move_to(211, 224, 86, 46, wait=True)
        self.device.move_to(114, 250, 20, 65, wait=True)
        self.device.move_to(-29, 256, 20, 96, wait=True)
        self.device.move_to(114, 250, 20, 65, wait=True)
        self.device.move_to(-29, 256, 20, 96, wait=True)
        self.device.move_to(114, 250, 20, 65, wait=True)
        self.device.move_to(-29, 256, 20, 96, wait=True)

        self.device.move_to(211, 224, 86, 46, wait=True)

    def emergency_stop(self) -> bool:
        try:
            self.device.move_to(228, 0, 151, 0, wait=True)
            return True
        except Exception as err:
            print(f"This error occuried: {err}")
            return False
