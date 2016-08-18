# import packages
import numpy as np
import csv
from scipy.stats.mstats import kruskalwallis

class Searcher:
	def __init__(self, indexPath):
		self.indexPath = indexPath

	# def search(self, queryFeatures, limit = 10):
	def search(self, queryFeatures):
		# initialize dictionary of results
		# i'll probably end up removing that limit (NO LIMIT!!!!!!) because we'll just want all possible results, probably ranked by similarity with the hope that everything we can't use is at the bottom and we can just find the cutoff point
		results = {}

		with open(self.indexPath) as f:
			reader = csv.reader(f)

			for row in reader:
				imagePath = row

			# for row in reader:
			# 	features = [float(x) for x in row[1:]]
			# 	d = self.chi2_distance(features, queryFeatures)

			# 	# update results dictionary with similarity metric
			# 	results[row[0]] = d

			# f.close()

		# sort results with smallest distances (most similar) are at the front
		results = sorted([(v, k) for (k, v) in results.items()])

		return results

	def chi2_distance(self, histA, histB, eps = 1e-10):
		d = 0.5 * np.sum([((a - b) ** 2) / (a + b + eps) for (a, b) in zip(histA, histB)])
		return d












