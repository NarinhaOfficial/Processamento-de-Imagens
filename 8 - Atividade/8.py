import cv2
import numpy as np

original = cv2.imread('noise.jpg')
tamanho = 7

kernel = np.ones((tamanho, tamanho), np.float32)/(tamanho*tamanho)
conv = cv2.filter2D(original, -1, kernel)
blur = cv2.blur(original, (tamanho,tamanho))
gauss = cv2.GaussianBlur(original,(tamanho, tamanho),0)
median = cv2.medianBlur(original, tamanho)

cv2.imshow('Original', original)
cv2.imshow('Convolution',conv)
cv2.imshow('Blur',blur)
cv2.imshow('GaussianBlur',gauss)
cv2.imshow('Median',median)

cv2.waitKey(0)
cv2.destroyAllWindows()