import cv2

def main():
    # Load the pre-trained face detection classifier
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    # Open the webcam
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: tidak dapat membuka kamera.")
        return
    
    print("Tekan 'q' untuk keluar dari jendela deteksi wajah.")

    while True:
        
        ret, frame = cap.read()  # Fixed: changed from `reed()` to `read()`

        if not ret:
            print("Error: Gagal membaca frame.")
            break

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Fixed: changed from `ractangle()` to `rectangle()`

        # Display the resulting frame
        cv2.imshow('Deteksi Wajah Real-time', frame)

        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the capture and destroy all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
