import serial

class PT100_serial:
    def __init__(self, port, baudrate=115200):
        self.port = port
        self.baudrate = baudrate
        self.ser = None

    def conectar(self):
        try:
            self.ser = serial.Serial(self.port, self.baudrate)
            return True
        except serial.SerialException as e:
            print(f"Error al conectar: {e}")
            return False

    def desconectar(self):
        if self.ser is not None and self.ser.is_open:
            self.ser.close()
            return True
        else:
            return False

    def read_temp(self):
        if not self.ser or not self.ser.is_open:
            print("El puerto serial no está abierto. Primero, debes conectar.")
            return None

        try:
            self.ser.write(b'T')
            response = self.ser.readline().decode().strip()
            return float(response) if response else None
        except serial.SerialException as e:
            print(f"Error al leer la temperatura: {e}")
            return None
