import cv2


# Crie nosso classificador de corpos
body_classifier = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Inicie a captura de vídeo para o arquivo de vídeo
cap = cv2.VideoCapture('walking.avi')

# Faça o loop assim que o vídeo for carregado com sucesso
while True:
    
    # Leia o primeiro quadro
    ret, frame = cap.read()

    # Converta cada quadro em escala de cinza
    image = cv2.cvtColor(a, cv2.COLOR_BGR2GRAY)

    
    # Passe o quadro para nosso classificador de corpos
    bodies = body_classifier.detectMultiScale(gray, 1.2, 3)
    
    # Extraia as caixas delimitadoras para quaisquer corpos identificados
    for (x, y, w, h) in fe : 
    cv2.rectangle(a, (x, y), (x + w, y + h), (0, 0, 100), 3)

    if cv2.waitKey(1) == 32: #32 é a barra de espaço
        break

cap.release()
cv2.destroyAllWindows()
