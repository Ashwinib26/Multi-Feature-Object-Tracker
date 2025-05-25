import cv2
import os

def process_tracking_image(filepath, filename, threshold):
    image = cv2.imread(filepath)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Using Shi-Tomasi corner detection
    corners = cv2.goodFeaturesToTrack(gray, 100, threshold, 10)
    corners = corners.astype(int)

    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(image, (x, y), 5, (0, 255, 0), -1)

    result_filename = f"processed_{filename}"
    result_path = os.path.join('static/results', result_filename)
    cv2.imwrite(result_path, image)

    stats = {
        'corners_detected': len(corners)
    }

    return result_path, stats
