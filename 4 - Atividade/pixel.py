import cv2
import numpy as np

original = cv2.imread('C:/Users/narin/OneDrive/Documentos/Programas/processamento de imagens/1 - Atividade/color_red.jpg')

#Para pegar as dimensões de altura e largura
altura, largura = original.shape[:2]

a = int(altura/2)
l = int(largura/2)

#cria um quadro negro com 3 canais de cores representados pelos valores de pixel
modificada = np.zeros((a, l, 3), np.uint8)

for linha in range (0, a):
    for coluna in range(0, l):
        modificada[linha,coluna] = original[linha*2, coluna*2]

cv2.imshow('Original', original)
cv2.imshow('Modificada', modificada)
cv2.waitKey(0)
cv2.destroyAllWindows()