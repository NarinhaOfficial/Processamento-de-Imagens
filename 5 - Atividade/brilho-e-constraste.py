'''▪Implemente um programa que realize o ajuste de brilho (teclas 'a' e 'z'), 
ajuste de contraste (teclas 's' e 'x') e aplique o efeito negativo (tecla 'n')'''
import cv2

original = cv2.imread('C:/Users/narin/OneDrive/Documentos/Programas/processamento de imagens/1 - Atividade/color_red.jpg')
modificar = cv2.imread('C:/Users/narin/OneDrive/Documentos/Programas/processamento de imagens/1 - Atividade/color_red.jpg')

brilho = 50
contraste = 1.5

while True:
    chave = cv2.waitKey(1)
    
    for a in range (original.shape[0]):
        for l in range (original.shape[1]):
            for c in range (original.shape[2]):
                if chave == ord('a'):
                    modificar[a, l, c] = min(255, modificar[a, l, c]+brilho)
                elif chave == ord('z'):
                    modificar[a, l, c] = max(0, modificar[a, l, c]-brilho)
                elif chave == ord('s'):
                    modificar[a, l, c] = min(255, modificar[a,l,c] * contraste)
                elif chave == ord('x'):
                    modificar[a, l, c] = max(0, modificar[a,l,c] / contraste)
                elif chave == ord('n'):
                    modificar[a, l, c] = 255 - modificar[a, l, c]
                elif chave == ord('m'):
                    modificar[a, l, c] = original [a,l,c]
                     
    cv2.imshow('a - Aumentar o brilho | z - Diminuir brilho | s - Aumentar o contraste | x - Diminuir o contraste | n - Aplicar negativo | m - Reverter todas as alterações', modificar)
    cv2.imshow('Original', original)
    
    
    if chave == ord('q'):
        break


cv2.waitKey(0)
cv2.destroyAllWindows()