# packages
from colordescriptor import ColorDescriptor
from searcher import Searcher
import csv
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be stored")
# ap.add_argument("-q", "--query", required = True,
# 	help = "Path to the query image")
ap.add_argument("-r", "--result-path", required = True,
	help = "Path to the result path")
args = vars(ap.parse_args())

with open(args["index"]) as f:
	reader = csv.reader(f)

	for row in reader:
		print row[1]
		result = cv2.imread(args["result_path"] + "/" + str(row[0]))
		# print row[1]
		# print args["result_path"] + "/" + row[0]
		cv2.imshow("Result",result)
		cv2.waitKey(0)

 
# image = 'opmex_u0.jpg'

# initialize the image descriptor
# cd = ColorDescriptor((8, 12, 3))

# load query image and get descriptor
# query = cv2.imread(args["query"])
# query = cv2.imread(image)
# features = cd.describe(query)



# perform the search
# searcher = Searcher(args["index"])
# results = searcher.search(features)

# cv2.imshow("Query", query)

# for (score, resultID) in results:
# 	print score
# 	result = cv2.imread(args["result_path"] + "/" + resultID)
# 	cv2.imshow("Result", result)
# 	cv2.waitKey(0)