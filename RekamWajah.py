import cv2
wajahDir = 'datawajah'
cam = cv2.VideoCapture(0)
cam.set(3, 640) #ubah lebar cam
cam.set(4, 480) #ubah tinggi cam
faceDetector = cv2.CascadeClassifier('haarcascade_eye.xml')
faceID = input("Masukan Face ID [ENTER]: ")
print("Proses Rekam Wajah.....")
ambilData = 0

while True:
    retV, frame = cam.read()
    abuAbu = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = faceDetector.detectMultiScale(abuAbu, 1.3, 5) #frame_selecFactor
    for (x, y, w, h) in faces:
        frame = cv2.rectangle(frame, (x, y), (x+w, y+h),(0,255,255),2)
        namaFile = 'wajah.'+str(faceID)+'.'+str(ambilData)+'.jpg'
        cv2.imwrite(wajahDir+'/'+namaFile,frame)
        ambilData += 1
    cv2.imshow('webcamku',frame)
    #cv2.imshow('webcamku 2', abuAbu)

    k = cv2.waitKey(1) & 0xFF
    if k  == 27 or k == ord('q'):
        break
    elif ambilData>30:
        break

print('Pengambilan data selesai')
cam.release()
cv2.destroyAllWindows()
