import cv2
import numpy as np

original = cv2.imread("10 - Atividade\ifmalogo.png")
modificada = cv2.imread("10 - Atividade\ifmalogo.png")
mascara = cv2.imread("mascara.jpg",0)

linhas, colunas = mascara.shape[:2]
roi = original[0:linhas, 0:colunas]

aplicando = cv2.inpaint(roi, mascara, 3, cv2.INPAINT_TELEA)
modificada[0:linhas, 0:colunas] = aplicando
cv2.imshow("Resultado", aplicando)

cv2.imshow("Original", original)
cv2.imshow("Máscara", mascara)
cv2.imshow("Modificada", modificada)

cv2.waitKey(0)
cv2.destroyAllWindows