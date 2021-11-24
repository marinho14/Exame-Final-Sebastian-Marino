import cv2
import numpy as np


def punto_1():
    ## llamo la imagen
    path = "soccer_game.png"
    image = cv2.imread(path)

    #calculo el histograma
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())
    # Peak mask
    lim_inf = (max_pos - 15, 0, 0)
    lim_sup = (max_pos + 15, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)

    ## aplico una erosion
    W = 1
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    ## Encuentro el porcentaje
    pix_blanco= np.where(mask)[0].shape[0]
    pix_totales= mask.shape[0]*mask.shape[1]
    porcentaje= (pix_blanco/pix_totales)*100
    print("El porcentaje de pixeles de la cancha es de {}%: ".format(porcentaje))
    cv2.imshow("Image2", mask)
    cv2.waitKey(0)

