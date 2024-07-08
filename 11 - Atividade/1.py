import cv2
import numpy as np

original = cv2.imread('11 - Atividade\image.png')
#criando um kernel
kernel = np.ones((3,3), np.uint8)
top_hat = cv2.morphologyEx(original, cv2.MORPH_TOPHAT, kernel)
black_hat = cv2.morphologyEx(original, cv2.MORPH_BLACKHAT, kernel)

while True:
    chave = cv2.waitKey(1)
    if chave == ord('q'):
        break
    cv2.imshow('Original', original)
    cv2.imshow('top hat', top_hat)
    cv2.imshow('black hat', black_hat)
print(kernel)
cv2.waitKey(0)
cv2.destroyAllWindows()