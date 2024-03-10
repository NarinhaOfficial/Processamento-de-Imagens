import cv2
import numpy as np

original = cv2.imread('1 - Atividade\color_red.jpg')
'''
shape[1] = largura
shape[0] = altura
'''
centro = (original.shape[1]/2, original.shape[0]/2)
giro = 45
#Iniciando a matriz
matriz = np.float32([[1,0,0], [0,1,0]])

while True:
    chave = cv2.waitKey(1)
    if chave == ord('r'):
        matriz = cv2.getRotationMatrix2D(centro, giro, 1)
        giro+=45
    modificada = cv2.warpAffine(original, matriz,(original.shape[1], original.shape[0]))
    cv2.imshow('Original', original)
    cv2.imshow('Modificada', modificada)
    if chave == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()