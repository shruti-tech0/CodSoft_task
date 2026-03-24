import cv2

def start_face_detection():
    print("Initializing webcam... Press 'q' to quit.")

    # 1. Load the pre-trained Haar Cascade face detection model built into OpenCV
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # 2. Start capturing video from the default webcam (index 0)
    video_capture = cv2.VideoCapture(0)

    # Check if the webcam opened successfully
    if not video_capture.isOpened():
        print("Error: Could not access the webcam.")
        return

    while True:
        # 3. Read the video frame-by-frame
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to grab frame.")
            break

        # 4. Convert the frame to Grayscale (Haar Cascades require grayscale images)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 5. Detect faces in the image
        # scaleFactor: Compensates for faces being closer or further away
        # minNeighbors: How many neighboring objects need to be detected to confirm it's a face
        faces = face_cascade.detectMultiScale(
            gray_frame, 
            scaleFactor=1.1, 
            minNeighbors=5, 
            minSize=(30, 30)
        )

        # 6. Draw a rectangle around the faces
        for (x, y, w, h) in faces:
            # cv2.rectangle(image, start_point, end_point, color(B,G,R), thickness)
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # 7. Display the resulting video feed with the drawn rectangles
        cv2.imshow('AI Face Detection - Press Q to Exit', frame)

        # 8. Listen for the 'q' key to stop the application
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting application...")
            break

    # 9. Release the webcam and close all OpenCV windows cleanly
    video_capture.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    start_face_detection()
