import sys
import re
import os


authors = {}


for line in sys.stdin:
	line = re.sub('[^a-z ]', ' ', line.lower())
	for word in line.split() :
 		print(word+","+str(1))
