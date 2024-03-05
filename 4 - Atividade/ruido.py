import random
import cv2
import numpy as np

original = cv2.imread('C:/Users/narin/OneDrive/Documentos/Programas/processamento de imagens/1 - Atividade/color_red.jpg')

valor = 0.00

while True:
    chave = cv2.waitKey(0)
    modificada = np.zeros(original.shape, np.uint8)
    modificada = cv2.imread('1 - Atividade\color_red.jpg')
    
  
    if chave == ord('a'):
        valor+=0.01
        barulho = 1 - valor
        for a in range(original.shape[0]):
            for l in range(original.shape[1]):
                sorteio = random.random()
                if sorteio<valor:
                    modificada[a][l] = 0
                elif sorteio > barulho:
                    modificada[a][l] = 255
                else:
                    modificada[a][l] = original[a][l]
        
 
    elif chave == ord('s'):
        if valor >= 0.01:
            valor -=0.01
            barulho = 1 - valor
            for a in range(original.shape[0]):
                for l in range(original.shape[1]):
                    sorteio = random.random()
                    if sorteio<valor:
                        modificada[a][l] = 0
                    elif sorteio > barulho:
                        modificada[a][l] = 255
                    else:
                        modificada[a][l] = original[a][l]
            

    cv2.imshow('Original', original)
    cv2.imshow('Sal e Pimenta', modificada)
    if chave == ord('q'):
        break
cv2.waitKey(0)
cv2.destroyAllWindows()