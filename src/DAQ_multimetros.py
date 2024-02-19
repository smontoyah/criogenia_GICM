import serial
import time

class Multimetro:
    def __init__(self, port):
        self.port = port
        self.serial = None

    def connect(self, baudrate=2400, timeout=10):
        self.serial = serial.Serial(None, baudrate=baudrate, timeout=timeout)

        if self.serial.isOpen():
            print(f"Se ha cerrado una sesión previa del puerto {self.port}")
            self.serial.close()

        self.serial.port = self.port
        self.serial.rts = False
        self.serial.open()
        time.sleep(1)
        print(f"Multímetro {self.port} está listo para recibir comandos.")
    

    def read_value(self):
        if self.serial is None or not self.serial.is_open:
            print(f"Error: El puerto {self.port} no está abierto.")
            return None

        self.serial.reset_input_buffer()
        bytes_recibidos = self.serial.readline()

        if len(bytes_recibidos) == 14:
    
            valor = float(bytes_recibidos[0:5].decode())
            potencia_10 = int(chr(bytes_recibidos[6]))
            multiplo = bytes_recibidos[9]

            if potencia_10 == 0:
                valor *= 1.0
            elif potencia_10 == 4:
                valor *= 0.1
            elif potencia_10 == 2:
                valor *= 0.01
            elif potencia_10 == 1:
                valor *= 0.001

            if multiplo == 128:  # 1000 0000
                valor *= 0.000001
            elif multiplo == 64:  # 0100 0000
                valor *= 0.001
            elif multiplo == 32:  # 0010 0000
                valor *= 1000
            elif multiplo == 16:  # 0001 0000
                valor *= 1000000

            return valor
        else:
            return 99999

    




