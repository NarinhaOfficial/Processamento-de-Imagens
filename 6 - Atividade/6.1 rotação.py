import cv2
import numpy as np

original = cv2.imread('1 - Atividade\color_red.jpg')
linhas, colunas = original.shape[:2]
giro = 45
M = np.float32([[1,0,0],[0,1,0]])

while True:
    chave = cv2.waitKey(1)

    if chave == ord('r'):
        M = cv2.getRotationMatrix2D(((colunas-1)/2.0,(linhas-1)/2.0),giro,1)
        giro+=45

    modificada = cv2.warpAffine(original, M,(colunas, linhas))
    cv2.imshow('Original', original)
    cv2.imshow('Modificada', modificada)
    if chave == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()