import cv2
import numpy as np

original = cv2.imread('1 - Atividade\color_red.jpg')
altura, largura = original.shape[:2]
centro = (largura/2, altura/2)
matriz = np.float32([[1,0,0],[0,1,0]])
giro = 0

while True:
    chave = cv2.waitKey(1)
    if chave == ord('d'):
        giro+=45
        matriz = cv2.getRotationMatrix2D(centro, giro, 1)

    elif chave == ord('e'):
        giro-=45
        matriz = cv2.getRotationMatrix2D(centro, giro, 1)
    modificada = cv2.warpAffine(original, matriz,(largura, altura))
    cv2.imshow('D - Direita, E - Esquerda', modificada)
    if chave == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()