# Importa a biblioteca necessária
import serial.tools.list_ports

# Define a classe Raspberry


class Raspberry:
    # Inicializa a classe
    def __init__(self) -> None:
        self.wait_time = 2  # Define o tempo de espera para a comunicação serial
        # Define a taxa de transmissão (baud rate) para a comunicação serial
        self.boud_rate = 115200

    # Envia um comando para a Raspberry Pi através da comunicação serial
    def send_command(self, command: str) -> bool:
        # Obtém a lista de portas seriais disponíveis
        available_ports = serial.tools.list_ports.comports()

        # Itera sobre todas as portas disponíveis
        for port in available_ports:
            # Exibe informações sobre a porta atual
            print(f"Porta = {port.device}, Descricao = {port.description}")
            try:
                # Tenta enviar o comando através da porta serial atual
                serial.Serial(str(port.device), self.boud_rate, timeout=self.wait_time).write(
                    bytes(str(command).encode()) + b"\n")
                # return True
            except Exception as err:
                # Se ocorrer um erro, exibe informações sobre o erro e tenta a próxima porta
                print(
                    f"Wrong port: {port.device}, this error captured: {err}, trying another one...")

        # Retorna False se não conseguir enviar o comando
        return False
