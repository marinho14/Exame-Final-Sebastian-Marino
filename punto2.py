import cv2

def punto_2():
    ## llamo la imagen
    path = "soccer_game.png"
    image = cv2.imread(path)
    image_draw = image.copy()

    # calculo el histograma
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hist_hue = cv2.calcHist([image_hsv], [0], None, [180], [0, 180])
    max_val = hist_hue.max()
    max_pos = int(hist_hue.argmax())
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Calculo la mascara
    lim_inf = (max_pos - 15, 0, 0)
    lim_sup = (max_pos + 15, 255, 255)
    mask = cv2.inRange(image_hsv, lim_inf, lim_sup)

    ## aplico una erosion para dejar solo los jugadores
    W = 2
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
    mask_eroded = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    W = 3
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2 * W + 1, 2 * W + 1))
    mask_dilated = cv2.morphologyEx(mask_eroded, cv2.MORPH_CLOSE, kernel)
    conteo=[] ## creo una lista para contar

    ## Encuentro los contornos
    contours, hierarchy = cv2.findContours(mask_dilated, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
    for idx, i in enumerate(contours):
        color = (0, 25, 100 + idx % 155)
        if cv2.contourArea(i) < 6000: ## No imprimo contronos grandes
            if cv2.contourArea(i) >600: ## No imprimo contornos pequeños
                #cv2.drawContours(image_draw, contours, idx, color, 2)
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(image_draw, (x, y), (x + w, y + h), (0, 0, 255), 3)
                conteo.append(1)  ## agrego 1 cada vez que cuento

    print("La cantidad de jugadores encontrada es:",len(conteo))
    cv2.imshow("Image2", image_draw)
    cv2.waitKey(0)


