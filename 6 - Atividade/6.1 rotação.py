import cv2
import numpy as np

original = cv2.imread('1 - Atividade\color_red.jpg')
linhas, colunas = original.shape[:2]
giro = 45
#Iniciando a matriz
M = np.float32([[1,0,0],[0,1,0]])
novo_centro = None

def detector(clique, x, y, flags, param):
    global novo_centro 
    if clique == cv2.EVENT_LBUTTONDOWN:
        novo_centro = (x,y)
cv2.imshow('Original', original)
cv2.setMouseCallback('Original', detector)

while True:
    chave = cv2.waitKey(1)

    if chave == ord('r') and novo_centro is not None:
        M = cv2.getRotationMatrix2D(novo_centro, giro, 1)
        giro+=45

    modificada = cv2.warpAffine(original, M,(colunas, linhas))
    
    cv2.imshow('Modificada', modificada)
    if chave == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()