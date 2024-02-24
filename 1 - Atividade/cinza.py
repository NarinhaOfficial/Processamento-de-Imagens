import cv2

imagem = cv2.imread('color_red.jpg')

altura, largura, canais = imagem.shape
x = 0
y = 0
for i in range(altura):
    for j in range(largura):
        if not (imagem[i, j, 2]>30 and imagem[i, j, 1]<60 and imagem[i, j, 0]<60):
            cinza = sum(imagem[i, j])//3
            imagem[i,j] = [cinza, cinza, cinza]
cv2.imshow('Tons de cinza', imagem)
cv2.waitKey(0)
cv2.destroyAllWindows()