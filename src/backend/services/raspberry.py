# Import the necessary library
import serial.tools.list_ports

# Define the Raspberry class
class Raspberry:
    # Initialize the class
    def __init__(self) -> None:
        self.wait_time = 2  # Set the wait time for serial communication
        # Set the transmission rate (baud rate) for serial communication
        self.boud_rate = 115200

    # Send a command to the Raspberry Pi through serial communication
    def send_command(self, command: str) -> bool:
        # Get the list of available serial ports
        available_ports = serial.tools.list_ports.comports()

        # Iterate over all available ports
        for port in available_ports:
            # Display information about the current port
            print(f"Port = {port.device}, Description = {port.description}")
            try:
                # Try to send the command through the current serial port
                serial.Serial(str(port.device), self.boud_rate, timeout=self.wait_time).write(
                    bytes(str(command).encode()) + b"\n")
                # return True
            except Exception as err:
                # If an error occurs, display information about the error and try the next port
                print(
                    f"Wrong port: {port.device}, this error captured: {err}, trying another one...")

        # Return False if unable to send the command
        return False
