from serial.tools import list_ports

import pydobot

# Checking ports of your computer
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[2].device
print(available_ports)
# Instance of your dobot connection
device = pydobot.Dobot(port=port, verbose=False)

(x, y, z, r, j1, j2, j3, j4) = device.pose()


def first_tray():
    print(f'x:{x} y:{y} z:{z} r:{r} j1:{j1} j2:{j2} j3:{j3} j4:{j4}')

    # Return to home
    device.move_to(228, 0, 151, 0, wait=True)

    device.move_to(203, -283,
               109, -53, wait=True)
    
    device.move_to(-94, -333,
               85, -105, wait=True)
    
    device.move_to(112, -331,
               75, -71, wait=True)

    device.move_to(112, -254,
               82, -65, wait=True)

    device.move_to(-96, -261,
               80, -110, wait=True)

    device.move_to(-96, -198,
               90, -115, wait=True)

    device.move_to(113, -212,
               87, -61, wait=True)

    device.move_to(203, -283,
            109, -53, wait=True)
    
def second_tray():
    # Return to home
    device.move_to(228, 0, 151, 0, wait=True)

    device.move_to(237, -70, 28, -16, wait=True)

    device.move_to(235, 88, 24, 21, wait=True)

    device.move_to(237, -70, 28, -16, wait=True)

    device.move_to(235, 88, 24, 21, wait=True)

    device.move_to(237, -70, 28, -16, wait=True)

    device.move_to(235, 88, 24, 21, wait=True)

    # Return to home
    device.move_to(228, 0, 151, 0, wait=True)



def third_tray():

    device.move_to(211, 224, 86, 46, wait=True)
    device.move_to(114, 250, 20, 65, wait=True)
    device.move_to(-29, 256, 20, 96, wait=True)
    device.move_to(114, 250, 20, 65, wait=True)
    device.move_to(-29, 256, 20, 96, wait=True)
    device.move_to(114, 250, 20, 65, wait=True)
    device.move_to(-29, 256, 20, 96, wait=True)

    device.move_to(211, 224, 86, 46, wait=True)
    # Return to home
    device.move_to(228, 0, 151, 0, wait=True)

first_tray()
second_tray()
third_tray()

device.close()
