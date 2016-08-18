import cv2
import numpy as np
from matplotlib import pyplot as plt

filename = 'amhow_u3.jpg'

img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)

corners = cv2.goodFeaturesToTrack(gray, 25, 1, 0.001, 10)
corners = np.int0(corners)

for i in corners:
	x,y = i.ravel()
	cv2.circle(img, (x,y), 3, 255, -1)

plt.imshow(img), plt.show()

# dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# dst = cv2.dilate(dst, None)

# img[dst > 0.01*dst.max()] = [0, 0, 255]
# cv2.imshow('dst', img)

# # time.sleep(10)

# # cv2.destroyAllWindows()
# if cv2.waitKey(0) & 0xff == 27:
# 	cv2.destroyAllWindows()