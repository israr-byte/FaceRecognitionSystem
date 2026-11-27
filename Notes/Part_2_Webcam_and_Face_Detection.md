# Part 2: Webcam and Face Detection

## Practical 2.1: Webcam Access Using OpenCV

### Objective
To access the computer webcam using Python and OpenCV and display live video.

### Library Used
- OpenCV (cv2)

### Important Functions
- cv2.VideoCapture(0): Opens the default webcam.
- camera.read(): Captures video frames.
- cv2.imshow(): Displays video frames.
- cv2.waitKey(): Checks keyboard input.
- camera.release(): Releases the webcam.
- cv2.destroyAllWindows(): Closes OpenCV windows.

### Result
Successfully accessed the webcam and displayed a real-time video stream.

---

## Practical 2.2: Real-Time Face Detection Using Haar Cascade

### Objective
To detect human faces in live webcam video using the Haar Cascade Classifier.

### Algorithm Used
Haar Cascade Classifier

### Model File
haarcascade_frontalface_default.xml

### Steps
1. Load the pre-trained Haar Cascade model.
2. Open the webcam.
3. Capture video frames.
4. Convert each frame to grayscale.
5. Detect faces using detectMultiScale().
6. Draw bounding boxes around detected faces.
7. Display the number of detected faces.
8. Release the camera and close the windows.

### Important Functions
- cv2.CascadeClassifier(): Loads the face detection model.
- cv2.cvtColor(): Converts the image to grayscale.
- detectMultiScale(): Detects faces in the image.
- cv2.rectangle(): Draws bounding boxes.
- cv2.putText(): Displays text on the frame.

### Parameters
- scaleFactor = 1.1
- minNeighbors = 5
- minSize = (30, 30)

### Result
Successfully detected faces in real-time webcam video and displayed green rectangles around faces with a face count.

### Project Files
- camera.py
- face_detection.py

### Progress
Completed webcam testing and real-time face detection.
Next: Face dataset collection and preprocessing.