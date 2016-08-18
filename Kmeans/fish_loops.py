# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import color_extract as ce
import cv2
import time
import glob
import csv
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-f", "--folder", required = True, help = "Path to the folder of images")
ap.add_argument("-c", "--clusters", required = True, type = int,
	help = "# of clusters")
args = vars(ap.parse_args())

# read all jpgs from folder
imageDir = glob.glob(args["folder"] + '*.jpg')
zippy = []

for i in range(len(imageDir)):
	savename = imageDir[i][2:len(imageDir[i])-4]
	new = ce.color_extract(imageDir[i], args["clusters"])
	zippy.append(new)
	plt.savefig(savename + '_ce.png')
	plt.close("all")

num = args["clusters"]
colnames = ['P', 'R', 'G', 'B']
header = ['ID']

for i in range(num):
	for j in range(len(colnames)):
		header.append(colnames[j]+str(i+1))

with open('out.csv', 'wb') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(zippy)