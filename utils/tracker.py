import cv2
import numpy as np
import os

def process_tracking_image(ref_path, target_path, ref_filename, target_filename):
    img1 = cv2.imread(ref_path, cv2.IMREAD_GRAYSCALE)  # Reference image (object)
    img2 = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)  # Target image (scene)

    orb = cv2.ORB_create(nfeatures=1000)

    # Find the keypoints and descriptors
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # Match using BFMatcher
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    # Draw first 30 matches
    match_img = cv2.drawMatches(
        img1, kp1, img2, kp2, matches[:30], None, flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
    )

    result_filename = f"tracked_{target_filename}"
    result_path = os.path.join('static/results', result_filename)
    cv2.imwrite(result_path, match_img)

    stats = {
        'total_matches': len(matches),
        'top_matches_drawn': 30
    }

    return result_path, stats
