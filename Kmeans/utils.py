# packages
import numpy as np
import cv2

def remove_bg(clt):

	base = 5
	labels = clt.labels_
	clusters = clt.cluster_centers_

	index = []
	for cluster in range(len(clusters)):
		old_cluster = clusters[cluster]
		new_cluster = []

		for i in np.nditer(old_cluster):
			new_cluster.append(int(base * round(float(i)/base)))

		if new_cluster == [0, 255, 0]:
			index.append(cluster)

	clusters = np.delete(clusters, index, 0)
	# labels = np.delete(labels, index, 0)

	numLabels = np.arange(0, len(np.unique(labels)) + 1)
	(hist, _) = np.histogram(clt.labels_, bins = numLabels)
	hist = hist.astype("float")
	hist = np.delete(hist, index, 0)
	hist /= hist.sum()

	return zip(hist, clusters)

def plot_colors(zippy):
	bar = np.zeros((50, 300, 3), dtype = "uint8")
	startX = 0

	# loop over pct of each cluster and color of cluster
	for (percent, color) in zippy:
		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX), 0), (int(endX), 50), color.astype("uint8").tolist(), -1)
		startX = endX

	# return the bar chart
	return bar


