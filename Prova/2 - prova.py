import cv2
import numpy as np
from matplotlib import pyplot as plt

original = cv2.imread('Prova/Original.png', 0)
imagem_colorida = cv2.cvtColor(original, cv2.COLOR_GRAY2BGR)

bordas = cv2.Canny(original, 50, 100)

contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

kernel = np.ones((3, 3), np.uint8)
erosion = cv2.erode(original, kernel, iterations=1)

for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)
    aprox = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
    if len(aprox) == 4:
        cv2.drawContours(imagem_colorida, [aprox], -3, (0, 255, 0), 5)
cv2.imshow('Quadrados', imagem_colorida)
cv2.waitKey(0)
cv2.destroyAllWindows()