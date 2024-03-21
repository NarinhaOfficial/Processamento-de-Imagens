import cv2
import numpy as np

logo = cv2.imread('7 - Atividade\logo-if.jpg')
imagem = cv2.imread('7 - Atividade\ifma-caxias.jpg')

# Serve para redimensionar a imagem
logo_if = cv2.resize(logo, (200, 100), interpolation=cv2.INTER_AREA)

linhas, colunas = logo_if.shape[:2]

local = imagem[:linhas, :colunas]

cinza = cv2.cvtColor(logo_if, cv2.COLOR_BGR2GRAY)
#125 é o valor mínimo e 255 é o valor máximo, o resultado ficará na invertida
ret, invertida = cv2.threshold(cinza, 125, 255, cv2.THRESH_BINARY)
mascara = cv2.bitwise_not(invertida) 

local[mascara != 0] = logo_if[mascara != 0]
imagem[:linhas, :colunas] = local
cv2.imshow('imagem', imagem)
cv2.imwrite('mascara.jpg', mascara)

cv2.waitKey(0)
cv2.destroyAllWindows()