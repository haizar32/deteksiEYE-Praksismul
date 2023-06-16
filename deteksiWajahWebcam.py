import cv2
cam = cv2.VideoCapture(0)
cam.set(3, 640) #ubah lebar
cam.set(4, 480) #ubah tinggi
faceDetector = cv2.CascadeClassifier('haarcascade_eye.xml')
while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5) #frame_selecFactor
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,255),2)
    cv2.imshow('webcamku',frame)
    #cv2.imshow('webcamku 2', abuAbu)

    k = cv2.waitKey(1) & 0xFF
    if k  == 27 or k == ord('q'):
        break
cam.relase()
cv2.destroyAllWindows()
