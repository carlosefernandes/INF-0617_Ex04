import sys
import re
import csv
import os

#f = open('/tmp/data/master_list.csv')
f = open('../master_list.csv')
reader = csv.reader(f)

book_authors = {}
author_words = {}
words = set()

# skip header lines
for i in range(5):
    next(reader)

# process in line
for row in reader :
	book_authors[row[4]] = row[3]


with open("index.txt", "r") as f:
	for line in f:
		line = line.replace("\n","") 
		words.add(line)


for line in sys.stdin:
	file = os.environ['mapreduce_map_input_file']
	prefix, file = file.split("u-")
	line = re.sub('[^a-z ]', ' ', line.lower())
	if book_authors[file] not in author_words.keys():
		author_words[book_authors[file]] = {}
	for word in line.split() :
		if word not in author_words[book_authors[file]].keys():
			value = 0
			if (word not in words):
				value = 1
			author_words[book_authors[file]][word] = value

for author in author_words.keys():
	for word in author_words[author].keys():
		print (author + "," + word + "," + str(author_words[author][word]))