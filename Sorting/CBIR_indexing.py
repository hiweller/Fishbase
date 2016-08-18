# import the necessary packages
from CBIR_classes import RGBHistogram
import argparse
import cPickle
import glob
import cv2
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to be indexed")
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
ap.add_argument("-b", "--bins", required = True, help = "Number of bins to be stored for color histogram")
args = vars(ap.parse_args())

# initialize the index dictionary to store our our quantifed
# images, with the 'key' of the dictionary being the image
# filename and the 'value' our computed features
index = {}

desc = RGBHistogram([int(args["bins"])] * 3)

for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
	k = imagePath[imagePath.rfind("/") + 1:]

	image = cv2.imread(imagePath)
	features = desc.describe(image)
	index[k] = features

f = open(args["index"], "w")
f.write(cPickle.dumps(index))
f.close()