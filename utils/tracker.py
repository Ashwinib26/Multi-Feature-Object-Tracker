import cv2
import numpy as np
import os

RESULT_FOLDER = 'static/results'

def process_tracking_image(filepath, filename, threshold):
    # Load image
    img = cv2.imread(filepath)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Example: Harris corner detection with adjustable threshold
    dst = cv2.cornerHarris(img_gray, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, marking corners
    img[dst > threshold * dst.max()] = [0, 0, 255]

    # Save processed image
    result_path = os.path.join(RESULT_FOLDER, f"tracked_{filename}")
    cv2.imwrite(result_path, img)

    # Some stats to show
    count = np.sum(dst > threshold * dst.max())
    stats = {
        "corners_detected": int(count),
        "threshold": threshold
    }
    return result_path, stats
