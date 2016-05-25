# importing packages
from __future__ import print_function
import cv2

# load image + convert
image = cv2.imread('jurassic_world.jpg') # loading image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original', image)

# initialize AKAZE descriptor (?!?! lol) + detect keypoints
# extract local invariant descriptors from image
detector = cv2.AKAZE_create()
(kps, descs) = detector.detectAndCompute(gray, None)
print('keypoints: {}, descriptors: {}'.format(len(kps), descs.shape))

# draw keypoints on image
cv2.drawKeypoints(image, kps, image, (0, 255, 0))
cv2.imshow('Output', image)
cv2.waitKey(0)