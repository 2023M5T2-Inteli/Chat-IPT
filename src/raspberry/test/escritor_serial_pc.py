import serial.tools.list_ports
import time

tempo_espera = 2
taxa_transmissao = 115200


def find_coms():

    ports_found = serial.tools.list_ports.comports()
    print("[COM ports found]")
    for item in ports_found:
        print(str(item))

    return ports_found

find_coms()

comunicacao_serial = serial.Serial("COM5", taxa_transmissao, timeout = tempo_espera)


while True:
    valor = str(input("Digite o valor que deseja passar para o raspberry: "))
    comunicacao_serial.write(valor + b"\n") # Escreve "on" na serial
    print("Valor enviado!")


