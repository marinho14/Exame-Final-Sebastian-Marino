# This is a sample Python script.
import cv2
import numpy as np

from punto1 import punto_1
from punto2 import punto_2
from punto3 import punto_3


if __name__ == '__main__':
    while 1:
        punto = int(input("Ingrese el punto que desea observar, ingrese 4 si desea salir: "))
        if punto==1:
            punto_1()
        elif punto== 2:
            punto_2()
        elif punto== 3:
            punto_3()
        else:
            break


