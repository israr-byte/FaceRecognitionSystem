import cv2
import os

# Main dataset folder
dataset_path = "dataset"

# Processed dataset folder
processed_path = os.path.join(dataset_path, "processed")

# Standard image size
image_size = (200, 200)

# Check if dataset exists
if not os.path.exists(dataset_path):
    print("Dataset folder not found.")
    exit()

total_processed = 0

# Loop through each person's folder
for person_name in os.listdir(dataset_path):

    person_folder = os.path.join(dataset_path, person_name)

    # Skip files and the processed folder
    if not os.path.isdir(person_folder) or person_name == "processed":
        continue

    # Create output folder for this person
    output_folder = os.path.join(processed_path, person_name)
    os.makedirs(output_folder, exist_ok=True)

    print(f"\nProcessing images for: {person_name}")

    # Loop through the person's images
    for filename in os.listdir(person_folder):

        image_path = os.path.join(person_folder, filename)

        # Read the image
        image = cv2.imread(image_path)

        if image is None:
            print(f"Could not read: {filename}")
            continue

        # Convert to grayscale
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Resize to standard dimensions
        resized = cv2.resize(gray, image_size)

        # Normalize pixel values
        normalized = cv2.normalize(
            resized,
            None,
            0,
            255,
            cv2.NORM_MINMAX
        )

        # Save processed image
        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, normalized)

        total_processed += 1

print("\nPreprocessing completed!")
print(f"Total images processed: {total_processed}")
print(f"Processed images saved in: {processed_path}")