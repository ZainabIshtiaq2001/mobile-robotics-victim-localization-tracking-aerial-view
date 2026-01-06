import cv2
import numpy as np
import random

# --------------------------------------------------
# LOAD RANDOM FRAME
# --------------------------------------------------
img = cv2.imread("random_frame.png")
if img is None:
    raise FileNotFoundError("random_frame.png not found")

h, w = img.shape[:2]

# --------------------------------------------------
# IMAGE POINTS (pixels) — measured by you
# Order:
# bottom-left, bottom-right, top-left, top-right
# --------------------------------------------------
image_pts = np.array([
    [23, 375],    # bottom-left
    [740, 403],   # bottom-right
    [99, 93],     # top-left
    [733, 132]    # top-right
], dtype=np.float32)

# --------------------------------------------------
# WORLD POINTS (meters) — rectangular ground plane
# Origin at top-left
# --------------------------------------------------
world_pts = np.array([
    [0.0, 5.5],     # bottom-left
    [11.5, 5.5],    # bottom-right
    [0.0, 0.0],     # top-left
    [11.5, 0.0]     # top-right
], dtype=np.float32)

# --------------------------------------------------
# COMPUTE HOMOGRAPHY (image to world)
# --------------------------------------------------
H, _ = cv2.findHomography(image_pts, world_pts)

print("Homography matrix (image to world):\n", H)

# --------------------------------------------------
# SELECT A RANDOM IMAGE POINT
# --------------------------------------------------
rand_x = random.randint(0, w - 1)
rand_y = random.randint(0, h - 1)

rand_pixel = np.array([[[rand_x, rand_y]]], dtype=np.float32)

# --------------------------------------------------
# PROJECT RANDOM POINT TO WORLD COORDINATES
# --------------------------------------------------
world_est = cv2.perspectiveTransform(rand_pixel, H)
Xw, Yw = world_est[0, 0]

print(f"\nRandom image point (px): ({rand_x}, {rand_y})")
print(f"Mapped world coordinate (m): X = {Xw:.2f}, Y = {Yw:.2f}")

# --------------------------------------------------
# ANNOTATION
# --------------------------------------------------
annotated = img.copy()

# Draw ground reference points
for i, (pt_img, pt_w) in enumerate(zip(image_pts, world_pts)):
    x, y = int(pt_img[0]), int(pt_img[1])
    cv2.circle(annotated, (x, y), 6, (255, 0, 0), -1)
    cv2.putText(
        annotated,
        f"W{tuple(pt_w)}",
        (x + 5, y - 5),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.45,
        (255, 0, 0),
        1
    )

# Draw random image point
cv2.circle(annotated, (rand_x, rand_y), 8, (0, 0, 255), -1)
cv2.putText(
    annotated,
    f"Img ({rand_x},{rand_y})",
    (rand_x + 5, rand_y - 5),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.5,
    (0, 0, 255),
    1
)

# Display mapped world coordinates
cv2.putText(
    annotated,
    f"World (X={Xw:.2f} m, Y={Yw:.2f} m)",
    (20, 30),
    cv2.FONT_HERSHEY_SIMPLEX,
    0.8,
    (0, 255, 0),
    2
)

# --------------------------------------------------
# SHOW & SAVE RESULT
# --------------------------------------------------
cv2.imshow("Victim Localization via Homography", annotated)
cv2.imwrite("random_frame_annotated.png", annotated)

cv2.waitKey(0)
cv2.destroyAllWindows()