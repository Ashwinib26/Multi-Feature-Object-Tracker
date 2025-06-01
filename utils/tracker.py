import cv2
import numpy as np
import os

def process_tracking_image(ref_path, target_path, ref_filename, target_filename, min_match_count=10):
    img1 = cv2.imread(ref_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(target_path, cv2.IMREAD_GRAYSCALE)

    orb = cv2.ORB_create(nfeatures=1000)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    if des1 is None or des2 is None:
        return None, {'detected': False, 'reason': 'No descriptors found', 'total_matches': 0, 'top_matches_drawn': 0}

    des1 = np.float32(des1)
    des2 = np.float32(des2)

    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)

    flann = cv2.FlannBasedMatcher(index_params, search_params)
    matches = flann.knnMatch(des1, des2, k=2)

    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    if len(good_matches) >= min_match_count:
        src_pts = np.float32([kp1[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
        dst_pts = np.float32([kp2[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
        matchesMask = mask.ravel().tolist()

        inlier_matches = [m for m, keep in zip(good_matches, matchesMask) if keep]

        match_img = cv2.drawMatches(img1, kp1, img2, kp2, inlier_matches[:30], None,
                                    matchColor=(0, 255, 0),
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)

        result_filename = f"tracked_{target_filename}"
        result_path = os.path.join('static/results', result_filename)
        cv2.imwrite(result_path, match_img)

        return result_path, {
            'detected': len(inlier_matches) >= min_match_count,
            'total_matches': len(inlier_matches),
            'top_matches_drawn': min(len(inlier_matches), 30)
        }
    else:
        match_img = cv2.drawMatches(img1, kp1, img2, kp2, good_matches[:30], None,
                                    matchColor=(0, 0, 255),
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
        result_filename = f"tracked_{target_filename}"
        result_path = os.path.join('static/results', result_filename)
        cv2.imwrite(result_path, match_img)

        return result_path, {
            'detected': False,
            'total_matches': len(good_matches),
            'top_matches_drawn': min(len(good_matches), 30)
        }
