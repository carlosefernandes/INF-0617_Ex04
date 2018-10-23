import sys
import re
import csv
import os

#f = open('/tmp/data/master_list.csv')
f = open(sys.argv[1])
reader = csv.reader(f)

book_authors = {}
author_words = {}
words = set()

# skip header lines
for i in range(5):
    next(reader)

# process in line
for row in reader :
	book_authors[row[4]] = row[3].lower()


with open(sys.argv[2], "r") as f:
	for line in f:
		line = line.replace("\n","").replace(" ","").replace("\t","")
		words.add(line)

for line in sys.stdin:
	file = os.environ['mapreduce_map_input_file']
	prefix, file = file.split("u-")
	line = re.sub('[^a-z ]', ' ', line.lower())
	if file not in book_authors.keys(): continue;
	author=book_authors[file]
	if author not in author_words.keys():
		author_words[author] = []
	for word in line.split() :
		if word not in author_words[author]:
			author_words[author].append(word)
			if (word in words):
				print(author + "," + word + ",0")
			else:
				print(author + "," + word + ",1")