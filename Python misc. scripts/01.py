# LOTR CBIR system (lesson 01)
# from http://www.pyimagesearch.com/2014/01/27/hobbits-and-histograms-a-how-to-guide-to-building-your-first-image-search-engine-in-python/

# packages
# from pyimagesearch.rgbhistogram import RGBHistogram
import argparse
import cPickle
import glob
import numpy as np
import cv2

class RGBHistogram:
	def __init__(self, bins):
		# store number of bins the histogram will use
		self.bins = bins

	def describe(self, image):
		# computes a 3D histogram in RGB, normalizes (scale-free)
		hist = cv2.calchist([image], [0, 1, 2],
			None, self.bins, [0, 256, 0, 256, 0, 256])
		hist = cv2.normalize(hist)

		# return 3D histogram as flattened 2D array
		return hist.flatten()


ap = argparse.ArgumentParser() # constructing "argument parser?"
ap.add_argument('-d', '--dataset', required = True,
	help = 'Path to the directory that contains the images to be indexed')
ap.add_argument('-i', '--index', required = True,
	help = 'Path for storing computed indices')
args = vars(ap.parse_args())