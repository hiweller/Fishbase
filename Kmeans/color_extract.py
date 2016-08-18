# import the necessary packages
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import argparse
import utils
import cv2
import time

def color_extract(img, clusters):
	image = cv2.imread(img)
	image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
 
 	fig, (ax1, ax2) = plt.subplots(2, 1)

 	im1 = ax1.imshow(image)
 	plt.axis("off")

	# show our image
	# plt.figure()
	# plt.axis("off")
	# plt.imshow(image)

	# reshape into pixel matrix
	image = image.reshape((image.shape[0] * image.shape[1], 3))
	
	# cluster using kmeans package
	clt = KMeans(n_clusters = (clusters+1))
	clt.fit(image)
	zippy = utils.remove_bg(clt)

	# zippy = utils.centroid_histogram(clt)
	bar = utils.plot_colors(zippy)

	im2 = ax2.imshow(bar)

	plt.axis("off")
	# plt.show()
	zippy = sorted(zippy, reverse = True)
	zippy = [i for j in zippy for i in j]
	zippy = [i for j in zippy for i in j.flatten('F')]
	zippy.insert(0, img[2:len(img)-4])

	return zippy