"""
SISTEMA AUTOMÁTICO DE INMERSIÓN Y MEDICIÓN GICM

Este script hace automatiza la adquisicion de datos y el control de un sistema de inmersion
en nitrógeno liquido para pruebas de componentes electrónicos y materiales a baja temperatura.
El sistema de medición y adquisicion consta de tres multimetros con conexion serial. Uno se 
utiliza para la medición de la temperatura, otro para corriente y otro para voltaje.
El control del motor se realiza a traves de comunicacion serial con un arduino en el que corre
el firmware "nema_criogenia_calibrado" y solo recibe el valor en cm que se quiera desplazar el sistema
para cada medida de T, I, V.

Para llevar el motor a una posicion determinada, ejecutar el codigo "GUI.py" y escribir el valor en cm
con la convencion de - hacia abajo


Sebastian Montoya 2023
"""
import time
import numpy as np
import matplotlib.pyplot as plt
from DAQ_multimetros import Multimetro
from motor_paso import MotorPaso

if __name__ == "__main__":
    


    n_lecturas = 10 # numero de lecturas que se desee realizar
    interval = 10 # tiemp0 en segundos que se espera para que se estabilice la temperatura
    dy = -1 #valor de paso de motor en cm (- hacia abajo)


    motor = MotorPaso("COM9")  # Revisar el puerto del arduino nano 
    multimetro1 = Multimetro("COM23")
    #multimetro2 = Multimetro("COM24")
    #multimetro3 = Multimetro("COM25")

    motor.conectar()
    multimetro1.connect()
    #multimetro2.connect()
    #multimetro3.connect()

    values1 = []  # Limpiar los valores anteriores
    values2 = []
    values3 = []
    for _ in range(n_lecturas):
        values_temporal = []
        for _ in range(int(interval)):
            valor1_temporal = multimetro1.read_value()
            values_temporal.append(valor1_temporal)
            mean_value = np.mean(values_temporal)
            print(mean_value)
        values1.append(mean_value)
        time.sleep(interval)
        valor1 = multimetro1.read_value()
        #valor2 = multimetro1.read_value()
        #valor3 = multimetro1.read_value()
        values1.append(valor1)
        #values2.append(valor2)
        #values3.append(valor2)
        motor.enviar_numero(dy)
        time.sleep(interval)

    print(f"Valores del Multímetro 1: {values1}")
    #print(f"Valores del Multímetro 1: {values2}")
    #print(f"Valores del Multímetro 1: {values3}")
    motor.desconectar()

    plt.plot(values1)
    plt.title("Height vs Temperature")
    plt.ylabel("T [°C]")
    plt.xlabel("t [s]")
    plt.grid()
    plt.show()

    
    
    
    
    