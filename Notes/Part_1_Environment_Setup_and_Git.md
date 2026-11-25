# FACE RECOGNITION SYSTEM USING OPENCV
## Part 1: Environment Setup and Git Practical Notes

**Student:** Israr Fatima  
**Project:** Face Recognition System  
**Programming Language:** Python  
**Tools:** OpenCV, NumPy, Git and GitHub

---

## 1. Introduction to the Project

The Face Recognition System is a computer vision project developed using Python and OpenCV.

The main purpose of this project is to detect and recognize human faces through a webcam.

The system will:
- Capture images using a webcam.
- Detect human faces.
- Process facial images.
- Extract facial features using PCA.
- Compare faces with stored data.
- Display the identity of recognized people.

## 2. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| OpenCV | Computer vision and image processing |
| NumPy | Numerical calculations |
| Haar Cascade | Face detection |
| PCA | Facial feature extraction |
| Git | Version control |
| GitHub | Online code hosting |

## 3. Python Environment Setup

### Step 1: Check Python version

Command:

```cmd
python --version
```

Output:

```text
Python 3.12.10
```

Purpose: Checks the installed Python version.

### Step 2: Create a project folder

Project folder:

```text
FaceRecognitionSystem
```

Purpose: Stores all project files in one location.

### Step 3: Create a virtual environment

Command:

```cmd
python -m venv .venv
```

Purpose: Creates an isolated Python environment for the project.

### Step 4: Activate the virtual environment

Command:

```cmd
.venv\Scripts\activate
```

After activation, the terminal displays:

```text
(.venv) C:\Users\3TEE\FaceRecognitionSystem>
```

Purpose: Activates the project's virtual environment.

## 4. Installing Required Libraries

### OpenCV

Command:

```cmd
pip install opencv-contrib-python
```

Purpose:
- Used for image processing.
- Used for video and webcam operations.
- Provides face recognition functionality through the contrib module.

### NumPy

Command:

```cmd
pip install numpy
```

Purpose:
- Performs mathematical calculations.
- Handles image arrays.
- Supports image processing operations.

## 5. Testing the Libraries

Python code:

```python
import cv2
import numpy as np

print(cv2.__version__)
print(np.__version__)
print(hasattr(cv2, "face"))
```

Verified output:

```text
5.1.0
2.5.5
True
```

Conclusion: OpenCV and NumPy were successfully installed and imported. The OpenCV face module was also available.

## 6. Introduction to Git

Git is a version control system used to track changes in project files.

It allows developers to:
- Save different versions of their work.
- Track changes.
- Restore previous versions.
- Collaborate with other developers.

## 7. Introduction to GitHub

GitHub is an online platform used to host Git repositories.

It allows developers to:
- Upload their projects.
- Share code.
- Collaborate with others.
- Maintain project history.

**Difference between Git and GitHub:**

Git is a version control tool, while GitHub is an online platform for hosting Git repositories.

## 8. Git Practical Implementation

### Step 1: Check Git installation

Command:

```cmd
git --version
```

Verified output:

```text
git version 2.55.0.windows.2
```

### Step 2: Configure Git username

Command:

```cmd
git config --global user.name "Israr Fatima"
```

Purpose: Sets the author name for Git commits.

### Step 3: Configure Git email

Command:

```cmd
git config --global user.email "israrfatima462@gmail.com"
```

Purpose: Sets the author email for Git commits.

### Step 4: Initialize Git repository

Command:

```cmd
git init
```

Output:

```text
Initialized empty Git repository
```

Purpose: Initializes Git tracking in the project folder.

### Step 5: Set the main branch

Command:

```cmd
git branch -M main
```

Purpose: Names the primary branch main.

### Step 6: Check repository status

Command:

```cmd
git status
```

Purpose: Displays modified, untracked, and staged files.

### Step 7: Add project files

Command:

```cmd
git add .gitignore README.md requirements.txt
```

Purpose: Adds selected files to the staging area.

### Step 8: Create the first commit

Command:

```cmd
git commit -m "Initial project setup and documentation"
```

Verified output:

```text
[main (root-commit) d0bb220]
3 files changed, 54 insertions(+)
```

Purpose: Saves the current staged changes as a project version.

### Step 9: Connect GitHub repository

Command:

```cmd
git remote add origin https://github.com/israr-byte/FaceRecognitionSystem.git
```

Purpose: Connects the local Git repository to the GitHub repository.

### Step 10: Verify remote connection

Command:

```cmd
git remote -v
```

Purpose: Displays the connected remote repository URLs.

### Step 11: Upload project to GitHub

Command:

```cmd
git push -u origin main
```

Purpose: Uploads the local main branch and its commits to GitHub.

Verified result:

```text
[new branch] main -> main
branch 'main' set up to track 'origin/main'
```

## 9. Git Ignore File

The `.gitignore` file tells Git which files and folders should not be tracked.

Example:

```text
.venv/
__pycache__/
*.py[cod]
dataset/
models/
.vscode/
```

Purpose:
- Prevents unnecessary files from being uploaded.
- Keeps the repository organized.
- Helps protect personal face datasets from accidental uploading.

## 10. Requirements File

The `requirements.txt` file contains the required Python packages.

Contents:

```text
opencv-contrib-python==5.1.0.95
numpy==2.5.5
```

To install all dependencies on another computer:

```cmd
pip install -r requirements.txt
```

## 11. Project Progress

Completed:
- Python environment setup.
- Virtual environment creation.
- OpenCV and NumPy installation.
- Library testing.
- Git configuration.
- Git repository initialization.
- First Git commit.
- GitHub connection.
- Successful project upload.

## 12. GitHub Repository

Repository URL:

https://github.com/israr-byte/FaceRecognitionSystem

## 13. Conclusion

In this practical session, I prepared the development environment for my Face Recognition System project. I installed the required libraries, configured Git, created a GitHub repository, and successfully uploaded the initial project files.

This setup provides the foundation for implementing face detection and recognition in the next development stages.

**Next Practical:** Webcam testing using Python and OpenCV.