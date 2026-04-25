import cv2
from deepface import DeepFace
import pyttsx3
import time


def speak_result(text):
    temp_engine = pyttsx3.init()
    temp_engine.setProperty('rate', 180)
    temp_engine.say(text)
    temp_engine.runAndWait()
    temp_engine.stop()


status_text = "Press ' S ' to Scan..."
is_Scanning = False
start_time = 0

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()
    if not ret:
        break
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    if is_Scanning:
        elapsed = time.time() - start_time

        if elapsed < 2:
            status_text = f"Analyzing...{int(2 - elapsed + 1)}"
        else:
            try:
                results = DeepFace.analyze(frame, actions=['emotion'], enforce_detection=False)
                emotion = results[0]['dominant_emotion']
                status_text = f"Results is :{emotion.upper()}"

                speak_result(f"I think you are feeling{emotion}")
                status_text = f"{emotion.upper()}. Press 'S' for next "

                is_Scanning = False
            except:
                emotion = "cant be analyzed"
                status_text = "Scan failed. Press S"
                is_Scanning = False

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.rectangle(frame, (x, y - 40), (x + w, y), (0, 255, 0), -1)
        cv2.putText(frame, status_text, (x + 5, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    cv2.imshow("Smart AI Assistant", frame)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('S') or key == ord('s'):
        is_Scanning = True
        start_time = time.time()

    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
