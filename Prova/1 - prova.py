import cv2
import numpy as np


original = cv2.imread('Prova\logo-if-vertical.png', cv2.IMREAD_UNCHANGED)
video = cv2.VideoCapture('Prova\ifma-480p.avi')

def func (original, largura = None, altura = None, inter = cv2.INTER_AREA):
    quadro = None
    (linhas, colunas) = original.shape[:2]

    if largura is None and altura is None:
        return original
    elif largura is None:
        resultado = altura/float(linhas)
        quadro = (int(colunas * resultado), altura)
    else:
        resultado = largura/float(colunas)
        quadro = (largura, int(linhas*resultado))
    r = cv2.resize(original, quadro, interpolation=inter)
    return r
lvideo = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
avideo = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
limg = int(lvideo*0.2)
aimg = int(limg/original.shape[1]) * original.shape[0]
while True:
    ret, frame = video.read()
    if not ret:
        break
    logo = func(original, largura=limg)

    aimg, limg = logo.shape[:2] 

    roi = frame[avideo - aimg- 10:avideo - 10, 10: limg + 10]

    mascara = logo[:, :, 3]

    frame[avideo - aimg - 10:avideo- 10, 10: limg + 10][mascara != 0] = \
    logo[:, :, :3] [mascara != 0]
    chave = cv2.waitKey(1)
    
    cv2.imshow('Video com a logo', frame)
    
    if chave == ord ('q'):
        break
video.release()

cv2.waitKey(0)
cv2.destroyAllWindows()