
import cv2

img = cv2.imread('fotos-teste/img1.jpg')
classifer = "haarcascade_frontalface_alt2.xml"


# carregando o algoritimo do classicador desejado
loadAlg = cv2.CascadeClassifier(cv2.data.haarcascades + classifer)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)


while not cv2.waitKey(20) & 0xFF == ord('q'):
    ret, frame_color = capture.read()
    gray = cv2.cvtColor(frame_color, cv2.COLOR_BGR2GRAY)
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = loadAlg.detectMultiScale(gray)
    for x, y, w, h in faces:
        cv2.rectangle(frame_color,(x,y), (x+w, y+h), (0,255,0),2)

    cv2.imshow('color', frame_color)
    # cv2.imshow('img', img)
    # cv2.imshow('gray', gray)


