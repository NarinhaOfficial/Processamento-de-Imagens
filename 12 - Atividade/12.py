import cv2

video = cv2.VideoCapture('IFMA Campus Caxias.mp4')
while True:
    ret, frame = video.read()
    if not ret:
        break

    canny = cv2.Canny(frame,100,120)
    canny = cv2.cvtColor(canny, cv2.COLOR_BGR2RGB)
    
    cv2.imshow('Teste', canny)
    chave = cv2.waitKey(1)
    if chave == ord('q'):
        break
    
video.release()
cv2.waitKey(0)
cv2.destroyAllWindows()