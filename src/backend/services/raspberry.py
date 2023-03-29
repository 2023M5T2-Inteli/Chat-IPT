import serial.tools.list_ports

class Raspberry:
    def __init__(self) -> None:
        self.wait_time = 2
        self.boud_rate = 115200

    def send_command(self, command: str) -> bool:
        available_ports = serial.tools.list_ports.comports()
        
        for port in available_ports:
            print(f"Porta = {port.device}, Descricao = {port.description}")
            try:
                serial.Serial(str(port.device), self.boud_rate, timeout = self.wait_time).write(bytes(str(command).encode()) + b"\n")
                # return True
            except Exception as err:
                print(
                    f"Wrong port: {port.device}, this error captured: {err}, trying another one...")
            
            
        return False