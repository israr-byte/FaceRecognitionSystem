import cv2
import os
import time

# Ask for the person's name
person_name = input("Enter person's name: ").strip().replace(" ", "_")

if not person_name:
    print("Name cannot be empty.")
    exit()

# Create a folder for this person's face images
dataset_path = os.path.join("dataset", person_name)
os.makedirs(dataset_path, exist_ok=True)

# Load the Haar Cascade face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# Open webcam
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Collection settings
max_images = 100
count = 0
last_capture_time = 0
capture_interval = 0.5  # Capture one image every half second

print("Face collection started!")
print("Look at the camera and move your face slightly.")
print("Press ESC to stop.")

while count < max_images:

    success, frame = camera.read()

    if not success:
        print("Could not read camera frame.")
        break

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # If a face is detected
    if len(faces) > 0:

        # Select the largest detected face
        x, y, w, h = max(faces, key=lambda face: face[2] * face[3])

        # Draw rectangle around face
        cv2.rectangle(
            frame,
            (x, y),
            (x + w, y + h),
            (0, 255, 0),
            2
        )

        # Capture only after the time interval
        current_time = time.time()

        if current_time - last_capture_time >= capture_interval:

            # Crop the face from grayscale image
            face_image = gray[y:y + h, x:x + w]

            # Resize face to a fixed size
            face_image = cv2.resize(face_image, (200, 200))

            # Create filename
            filename = f"face_{count + 1:03d}.jpg"

            # Save image
            file_path = os.path.join(dataset_path, filename)
            cv2.imwrite(file_path, face_image)

            count += 1
            last_capture_time = current_time

    # Display collection progress
    cv2.putText(
        frame,
        f"Images collected: {count}/{max_images}",
        (20, 40),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (0, 255, 0),
        2
    )

    cv2.imshow("Face Dataset Collection", frame)

    # Stop when ESC is pressed
    if cv2.waitKey(1) == 27:
        break

# Cleanup
camera.release()
cv2.destroyAllWindows()

print(f"Collection finished. {count} images saved.")
print(f"Dataset location: {dataset_path}")