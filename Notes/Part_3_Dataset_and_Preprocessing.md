# Part 3: Face Dataset Collection and Image Preprocessing

## Practical 3.1 — Face Dataset Collection

### Objective
To collect face images from a webcam and save them in an organized dataset for facial recognition.

### Tools
- Python
- OpenCV
- Haar Cascade face detector

### Implementation
1. Opened the webcam.
2. Detected faces using Haar Cascade.
3. Selected the largest detected face.
4. Cropped the face region.
5. Converted the crop to grayscale.
6. Resized the face image to 200 × 200.
7. Saved images in a folder named after the person.

### Result
Successfully collected face samples from the webcam and saved them locally in an organized dataset.

---

## Practical 3.2 — Image Preprocessing

### Objective
To prepare face images in a consistent format before training the recognition model.

### Preprocessing Steps
- Read the saved image.
- Convert to grayscale.
- Resize to 200 × 200 pixels.
- Normalize pixel intensity values to the range 0–255.
- Save processed images separately.

### Important Functions
- `os.listdir()` — lists files and folders.
- `cv2.imread()` — reads an image.
- `cv2.cvtColor()` — converts image color format.
- `cv2.resize()` — resizes an image.
- `cv2.normalize()` — normalizes image intensity values.
- `cv2.imwrite()` — saves an image.

### Result
Successfully preprocessed the face dataset and saved standardized images separately from the original samples.

### Files Created
- `collect_faces.py`
- `preprocess.py`

### Next Practical
Face labels and training the recognition model using PCA/Eigenfaces.
