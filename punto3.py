import cv2
import numpy as np


def punto_3():

    font = cv2.FONT_HERSHEY_SIMPLEX
    fontScale = 1
    color = (255, 0, 0)
    thickness = 2

    ## Se define la funcion de click
    def click(event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            points.append((x, y))

    points = [] ## Los puntos seleccionados por el usuario en las imagenes
    path = "soccer_game.png"
    image = cv2.imread(path)
    image_draw = np.copy(image)

    points  = []
    points1 = []
    points2 = []
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", click)
    W= image.shape[1]
    p=0

    ## Se define donde se debe graficar la linea
    point_counter = 0
    while True:
        cv2.imshow("Image", image_draw)
        key = cv2.waitKey(1) & 0xFF
        if len(points)==3:
            cv2.putText(image_draw, 'p' + str(p), (points[-1][0], points[-1][1]), font, fontScale, color, thickness,cv2.LINE_AA)
            points1 = points.copy()
            points = []
            break
        if len(points) > point_counter:
            point_counter = len(points)
            cv2.circle(image_draw, (points[-1][0], points[-1][1]), 3, [0, 0, 255], -1)
            cv2.putText(image_draw, 'p'+str(p), (points[-1][0], points[-1][1]), font,fontScale, color, thickness, cv2.LINE_AA)
            p=p+1


    ## Se encuentran los puntos X y Y de los puntos escogidos
    X_1= points1[0][0]
    Y_1= points1[0][1]

    X_2= points1[1][0]
    Y_2= points1[1][1]

    X_3= points1[2][0]
    Y_3= points1[2][1]

    ## Se encuentra la pendiente de la recta
    pendiente= (Y_2-Y_1)/(X_2-X_1)

    ## Se encuentra el desface de la recta
    b = Y_1-pendiente*X_1


    ## Se encuentran los puntos iniciales
    X_ini= 0
    X_final= W

    Y_ini= int(X_ini*pendiente+b)
    Y_final=int(X_final*pendiente+b)

    ## Se encuentra el desface de la otra recta
    b2 = Y_3-pendiente*X_3


    ##Se encuentran los parametros de la recta paralela
    Y_ini_2= int(X_ini*pendiente+b2)
    Y_final_2=int(X_final*pendiente+b2)

    azul = (255, 0, 0)   ## Se define el color magenta
    amarillo = (0, 255, 255)
    image = cv2.line(image_draw, (X_ini,Y_ini), (X_final,Y_final), azul, 2)
    image = cv2.line(image_draw, (X_ini,Y_ini_2), (X_final,Y_final_2), amarillo, 2)

    cv2.imshow("Image2", image)
    cv2.waitKey(0)