# menggunakan library open-Cv
import cv2

# siapin alat deteksi wajah
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_frontalface_default.xml')


# membaca kamera. 0 utk laptop/webcam / 1 utk cam lebih dari 2
cap = cv2.VideoCapture(0)


# cek kamera
if not cap.isOpened():
    print("Kamera kamu tidak bisa diakses!")
    exit()


# mulai baca video dan deteksi wajah
while True:
    ret, frame = cap.read()
    if not ret:
        print("Gagal membaca frame!")
        continue


# buat kotak di sekitar wajah kamu
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1,minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)



# tampilkan output program
    cv2.imshow('Deteksi wajah cuma 6 step check', frame)

    if cv2.waitKey(1) == ord('q'):
        break

