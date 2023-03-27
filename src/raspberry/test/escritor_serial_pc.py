import serial.tools.list_ports

# Some values to config the serial communication
tempo_espera = 2
taxa_transmissao = 115200

# Function to find the specific raspberry's port


def find_coms():
    # Get all ports available in your device
    ports_found = serial.tools.list_ports.comports()
    # Passing in each port to verify
    for port in ports_found:
        # Will only return the port that is available
        if port.description != "n/a":
            print(port.device)
            return port.device


# Storaging the port's name into the variable
porta = find_coms()
# Setting up the serial communication
comunicacao_serial = serial.Serial(
    str(porta), taxa_transmissao, timeout=tempo_espera)


while True:
    # Ask for the user to input some value into the terminal and this value is storaged in the variable
    valor = str(input("Digite o valor que deseja passar para o raspberry: "))
    # Send the value through the serial port configured in the variable "comunicacao_serial"
    comunicacao_serial.write(bytes(valor.encode()) + b"\n")
    # Some response for the user to confirm which value was sent
    print(f"Valor enviado! ---> {valor}")
