# Facial Recognition Attendance System

## 📌 Overview
This project is a facial recognition-based attendance system that detects and recognizes faces to mark attendance automatically. It is built using OpenCV and the `face_recognition` library.

## 🚀 Features
- **Real-time Face Detection**: Uses OpenCV to capture and detect faces from a live webcam feed.
- **Face Recognition**: Matches faces against a stored database.
- **Automated Attendance Marking**: Records attendance in a CSV file with timestamps.
- **Scalable**: Can be extended to support multiple users.

## 🛠️ Installation
### Prerequisites
Make sure you have the following installed:
- Python 3.7+
- OpenCV
- dlib
- face_recognition
- numpy

### Setup Instructions
1. Clone this repository:
   ```sh
   git clone https://github.com/SaayraPoswal25/Facial-Recognition.git
   cd Facial-Recognition
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Run the program:
   ```sh
   python attendance.py
   ```

## 📂 Project Structure
```
Facial-Recognition/
│── ImagesAttendance/    # Folder containing known faces
│── Attendance.csv       # Stores attendance records
│── attendance.py        # Main script
│── requirements.txt     # Required dependencies
│── README.md            # Project documentation
```

## 📸 Usage
1. Place images of people (with their names as filenames) inside the `ImagesAttendance/` folder.
2. Run `main.py`, and the system will start recognizing faces.
3. The system logs recognized faces in `attendance.csv` with timestamps.

## 🔧 Troubleshooting
- If `face_recognition` is not detecting faces, ensure that `face_recognition_models` is correctly installed.
- For OpenCV errors, verify that `cv2` is installed properly.

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 💡 Future Improvements
- Support for multiple cameras
- Web-based dashboard for attendance tracking
- Integration with database storage

## 🙌 Contributing
Pull requests are welcome! Feel free to fork this repository and submit improvements.
