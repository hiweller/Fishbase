# packages
import numpy as np
import argparse
import glob
import cv2

def auto_canny(image, sigma=0.05):
	# compute median pixel intensity for each channel
	v = np.median(image)

	# apply edge detection with computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)

	# return edged image
	return edged

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--images", required = True, help = "Path to input dataset of images")
args = vars(ap.parse_args())

# loop over images
for imagePath in glob.glob(args["images"] + "/*.jpg"):
	# load, convert to grayscale, apply Gaussian blur
	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	blurred = cv2.GaussianBlur(gray, (3, 3), 0)

	# use Canny edge detection - test out wide, narrow, and auto threshold
	wide = cv2.Canny(blurred, 10, 200)
	tight = cv2.Canny(blurred, 225, 250)
	auto = auto_canny(blurred)

	# show figs
	cv2.imshow("Original", image)
	cv2.imshow("Edges", auto)
	cv2.waitKey(0)