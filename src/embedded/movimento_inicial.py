from serial.tools import list_ports

import pydobot

# Checking ports of your computer
available_ports = list_ports.comports()
print(f'available ports: {[x.device for x in available_ports]}')
port = available_ports[2].device

# Instance of your dobot connection
device = pydobot.Dobot(port=port, verbose=False)

# Defining home
device_home = device.pose()

#
device_positon = device.pose()

# Primeiro movimento (max "x")
device.move_to(device_positon[0] + 65, device_positon[1] - 120,
               device_positon[2] - 150, device_positon[3], wait=True)
device_positon = device.pose()

# # Segundo movimento (max "y")
# device.move_to(device_positon[0], device_positon[1] - 120,
#                device_positon[2], device_positon[3], wait=True)
# device_positon = device.pose()

# # Terceiro movimento (min "z")
# device.move_to(device_positon[0], device_positon[1],
#                device_positon[2] - 150, device_positon[3], wait=True)
# device_positon = device.pose()

# Quarto movimento (min "y")
device.move_to(device_positon[0], device_positon[1] + 240,
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quarto movimento (second "x")
device.move_to(device_positon[0] - 40, device_positon[1],
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quinto movimento (second "y")
device.move_to(device_positon[0], device_positon[1] - 240,
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quarto movimento (third "x")
device.move_to(device_positon[0] - 40, device_positon[1],
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quinto movimento (third "y")
device.move_to(device_positon[0], device_positon[1] + 240,
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quarto movimento (fourth "x")
device.move_to(device_positon[0] - 40, device_positon[1],
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# Quinto movimento (fourth "y")
device.move_to(device_positon[0], device_positon[1] - 240,
               device_positon[2], device_positon[3], wait=True)
device_positon = device.pose()

# move_to(x, y, z, r, wait=False) queues a translation in dobot to given coordinates

# x: float x cartesian coordinate to move
# y: float y cartesian coordinate to move
# z: float z cartesian coordinate to move
# r: float r effector rotation
# wait: bool waits until command has been executed to return to process


# Back to home
device.move_to(device_home[0], device_home[1], device_home[2], device_home[3])
device.close()
