import cv2
import numpy as np

original = cv2.imread('9 - Atividade\clown.jpg')

#Seve para calcular a transformada de Fourier
calcular = np.fft.fft2(original)
#Serve para centralizar a frequência do espectro
centralizar = np.fft.fftshift(calcular)
#Serve para calcular a magnitude
magnitude = np.log(np.abs(centralizar))/20
raio = 10
mascara = np.ones_like(original)
altura = mascara.shape[0]//2
largura = mascara.shape[1]//2
cv2.rectangle(mascara, (largura-45,0), (largura-20, altura*2), (255,255,255), -1)[0]
cv2.rectangle(mascara, (largura+20,0), (largura+45, altura*2), (255,255,255), -1)[0]
mascara = 255-mascara
mascara = cv2.GaussianBlur(mascara, (3,3),0)

aplicando = np.multiply(centralizar, mascara)/255
inversa = np.fft.ifftshift(centralizar)
invertida = np.fft.ifftshift(aplicando)

filtrada = np.fft.ifft2(invertida)
filtrada = np.abs(1*filtrada).clip(0,255).astype(np.uint8)

cv2.imshow("Original", original)
cv2.imshow("Espectro", magnitude)
cv2.imshow("Mascara",mascara)
cv2.imshow("Filtrada",filtrada)

cv2.waitKey(0)
cv2.destroyAllWindows()