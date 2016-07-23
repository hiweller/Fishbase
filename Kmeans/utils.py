# packages
import numpy as np
import cv2

def centroid_histogram(clt):
	# grab number of clusters to make histogram based on pixel counts
	numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)

	# normalize the histogram such that it sums to 1
	hist = hist.astype("float")
	hist /= hist.sum()

	return hist

def plot_colors(hist, centroids):
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0

	# loop over pct of each cluster and color of cluster
	for (percent, color) in zip(hist, centroids):
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
		startX = endX

	# return the bar chart
	return bar