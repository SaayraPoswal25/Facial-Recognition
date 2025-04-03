import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime, timedelta

# Load images and encodings
path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(os.path.join(path, cl))
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if encode:
            encodeList.append(encode[0])  # Append only if encoding is found
    return encodeList

# Store the last recorded attendance time
last_attendance_time = datetime.now() - timedelta(seconds=10)

def markAttendance(name):
    """Marks attendance only if 30 seconds have passed since the last recorded entry."""
    global last_attendance_time
    current_time = datetime.now()

    if current_time - last_attendance_time < timedelta(seconds=10):
        return  # Skip marking attendance

    last_attendance_time = current_time

    with open('Attendance.csv', 'a') as f:
        dtString = current_time.strftime('%H:%M:%S')
        f.write(f'\n{name},{dtString}')

# Encode known faces once
encodeListKnown = findEncodings(images)
print('Encoding Complete')

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    if not success:
        continue  # Skip iteration if frame not captured

    # Resize and convert frame only once
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

    if not facesCurFrame:  
        # Skip processing if no faces are detected
        cv2.imshow('Webcam', img)
        cv2.waitKey(1)
        continue

    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace, tolerance=0.5)  # Keep strict tolerance
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        matchIndex = np.argmin(faceDis)

        name = "Unknown"

        if matches[matchIndex]:
            # Verify facial landmarks (focus on eyes and nose, as beards/turbans cover lower face)
            landmarks = face_recognition.face_landmarks(imgS)
            if landmarks:
                key_points = landmarks[0]  # Get first detected face's landmarks
                if "left_eye" in key_points and "right_eye" in key_points and "nose_tip" in key_points:
                    name = classNames[matchIndex].upper()

        if name != "Unknown":
            # Scale face locations back to original image size
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

            # Draw rectangle and text only when face is detected
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            # Mark attendance
            markAttendance(name)

    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
