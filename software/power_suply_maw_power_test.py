import cv2
import numpy as np
import time

width, height = 1920, 1080

print("Starting GPU stress test")

while True:
    # Allocate a large image
    img = np.random.randint(0, 255, (height, width, 3), dtype=np.uint8)

    # Heavy OpenCV operations (these use VideoCore GPU if compiled for it)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (25, 25), 0)
    edges = cv2.Canny(blurred, 50, 150)

    # Simulate rendering
    cv2.imshow("Stress", edges)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
