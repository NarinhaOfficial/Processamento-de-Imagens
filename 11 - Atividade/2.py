import cv2
import numpy as np

original = cv2.imread('11 - Atividade/2.png')
kernel = np.ones((0,0), np.uint8)
kernel2 = np.ones((0,0), np.uint8)

horizontal = np.ones((2,2), np.uint8)
vertical = np.ones((2,2), np.uint8) #altura, largura

t_horizontal = np.ones((4,1), np.uint8)
t_vertical = np.ones((0,7), np.uint8)

dilation = cv2.dilate(original, kernel, iterations = 10)

teste = cv2.morphologyEx(original, cv2.MORPH_OPEN, kernel)



while True:
    cv2.imshow('Original', original)
    chave = cv2.waitKey(1)
    if chave == ord('1'):
        erosion_vertical = cv2.erode(original, vertical, iterations = (10))
        erosion_horizontal = cv2.erode(erosion_vertical, horizontal, iterations=10)
        gradiente = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel)
        modificada = cv2.addWeighted(gradiente, 0.1, erosion_horizontal, 1, 0)
        cv2.imshow('modificada', modificada)
    if chave == ord('2'):
        t_erosion_vertical = cv2.erode(original, t_vertical, iterations = (10))
        t_erosion_horizontal = cv2.erode(t_erosion_vertical, t_horizontal, iterations=10)
        gradiente = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel2)
        t = cv2.addWeighted(gradiente, 0.1, t_erosion_horizontal, 1, 0)
        cv2.imshow('t',t)
    if chave == ord('3'):
        erosion = cv2.erode(original, kernel, iterations=10)
        gradiente = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel)
        modificada = cv2.addWeighted(gradiente, 1, dilation, 0.9, 0)
        cv2.imshow('erosão', modificada)
    if chave == ord('q'):
        break
    
    
    
cv2.waitKey(0)
cv2.destroyAllWindows()