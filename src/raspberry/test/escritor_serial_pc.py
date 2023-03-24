import serial.tools.list_ports

tempo_espera = 2
taxa_transmissao = 115200

def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for port in ports_found:
        if port.description != "n/a":
            print(port.device)
            return port.device


porta = find_coms()

comunicacao_serial = serial.Serial(str(porta), taxa_transmissao, timeout = tempo_espera)


while True:
    valor = str(input("Digite o valor que deseja passar para o raspberry: "))
    comunicacao_serial.write(bytes(valor.encode()) + b"\n") # Escreve "on" na serial
    print(f"Valor enviado! ---> {valor}")


