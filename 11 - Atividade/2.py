import cv2
import numpy as np

original = cv2.imread('11 - Atividade/2.png')
kernel = np.ones((0,0), np.uint8)
kernel2 = np.ones((0,0), np.uint8)

horizontal = np.ones((2,2), np.uint8)
vertical = np.ones((4,3), np.uint8) #altura, largura

t_horizontal = np.ones((2,2), np.uint8)
t_vertical = np.ones((4,1), np.uint8)

dilation = cv2.dilate(original, kernel, iterations = 10)
erosion_vertical = cv2.erode(original, vertical, iterations = (10))
erosion_horizontal = cv2.erode(erosion_vertical, horizontal, iterations=10)
gradiente = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel)
teste = cv2.morphologyEx(original, cv2.MORPH_OPEN, kernel)
modificada = cv2.addWeighted(gradiente, 0.1, erosion_horizontal, 1, 0)

t_erosion_vertical = cv2.erode(original, t_vertical, iterations = (10))
t_erosion_horizontal = cv2.erode(erosion_vertical, t_horizontal, iterations=10)
gradiente = cv2.morphologyEx(original, cv2.MORPH_GRADIENT, kernel2)
t = cv2.addWeighted(gradiente, 0.1, t_erosion_horizontal, 1, 0)
while True:
    cv2.imshow('Original', original)
    chave = cv2.waitKey(1)
    if chave == ord('q'):
        break
    cv2.imshow('dilation', dilation)
    #cv2.imshow('erosão', erosion)
    cv2.imshow('modificada', modificada)
    cv2.imshow('t',t)
cv2.waitKey(0)
cv2.destroyAllWindows()