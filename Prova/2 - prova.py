import cv2
import numpy as np
from matplotlib import pyplot as plt
# cv2.findContours()
# cv2.drawContours(original, )
# cv2.minEnclosingCircle()
original = cv2.imread('Prova\Original.png',0)
bordas = cv2.Canny(original, 50, 100)
contornos, _ = cv2.findContours(bordas, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
kernel = np.ones((3,3),np.uint8)
erosion = cv2.erode(original, kernel, iterations = 1)
for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)
    aprox = cv2.approxPolyDP(contorno, 0.02 * perimetro, True)
    if len(aprox) == 4:
        cv2.drawContours(original, [aprox], -1, (0, 255, 0), 3)
cv2.imshow('Original', original)
# plt.subplot(223), plt.imshow(erosion)
# plt.title('Erosion')
cv2.waitKey(0)
cv2.destroyAllWindows()
