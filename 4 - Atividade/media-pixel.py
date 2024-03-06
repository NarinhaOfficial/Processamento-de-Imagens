import cv2
import numpy as np

original = cv2.imread('1 - Atividade\color_red.jpg')
#Para pegar as dimensões de altura e largura
altura, largura = original.shape[:2]
#criar uma nova dimensão para a modificada
a = int(altura/2)
l = int(largura/2)
#Criar a matriz modificada com as novas dimensões e com os 3 canais de cores
modificada = np.zeros((a, l, 3), np.uint8)
#percorrer a modificada
for linha in range(0, a):
    for coluna in range(0, l):
        #acumula a soma dos valores dos pixels na vizinhança
        soma = np.zeros(3)
        #mantém a contagem de quantos pixels foram considerados na contagem durante o cálculo da média
        contador = 0
        #percorre uma matriz 2x2 dentro da modificada
        for i in range(0,2):
            for j in range(0,2):
                soma+= original[2*linha+i, 2*coluna+j]
                contador+=1
        modificada[linha, coluna] = soma / contador
cv2.imshow('Original', original)
cv2.imshow('Modificada', modificada)
cv2.waitKey(0)
cv2.destroyAllWindows()