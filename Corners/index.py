from colordescriptor import ColorDescriptor
import argparse
import glob
import cv2
import json
import csv
from scipy.stats.mstats import kruskalwallis

"""
Indexes a set of images by corner and center using a HSV color histogram and stores indices. Requires colordescriptor.py.
"""
# ap = argparse.ArgumentParser()
# ap.add_argument("-d", "--dataset", required = True,
# 	help = "Path to the directory that contains the images to be indexed")
# ap.add_argument("-i", "--index", required = True,
# 	help = "Path to where the computed index will be stored")
# args = vars(ap.parse_args())
dataset = 'Opistognathidae'
# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3)) # HSV binning -- 8 hue, 12 saturation, 3 value

# open output
# output = open(args["index"], "w")

kw = []

# loop over images
# for imagePath in glob.glob(args["dataset"] + "/*.jpg"):
for imagePath in glob.glob(dataset + "/*.jpg"):

	imageID = imagePath[imagePath.rfind("/") + 1:]
	image = cv2.imread(imagePath)

	# describe image
	features = cd.describe(image)
	

	temp = kruskalwallis(features)
	kw.append((imageID, temp[0], temp[1]))

	# kw = [str(f) for f in kw]
	# output.write("%s, %s\n" % (imageID, ",".join(kw)))	
	# features = [str(f) for f in features]
	# output.write("%s, %s\n" % (imageID, ",".join(features)))

# output = open(args["index"], "w")

# # order by 
# kw = sorted(kw, key=lambda l:l[1])

# with open(args["index"], 'wb') as f:
# 	wr = csv.writer(f)
# 	wr.writerows(kw)