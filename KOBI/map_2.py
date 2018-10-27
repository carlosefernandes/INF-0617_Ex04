import sys
import re
import csv
import os

FILE_MASTER_LIST = sys.argv[1] 	#master_list.csv
FILE_COM_WORDS   = sys.argv[2] 	#3000 most common words

f = open(FILE_MASTER_LIST, "r")
reader = csv.reader(f)

book_authors = {}
author_words = {}
words = set()

# skip header lines
for i in range(5):
    next(reader)

# Build dictionary of authors indexed by book
for row in reader :
	# Consider only book/author whose language is english
	if row[8] == "":
		# Replace "," by space in author name
		book_authors[row[4]] = row[3].lower().replace(","," ")

# Build set of popular words
with open(FILE_COM_WORDS, "r") as f:
	for line in f:
		line = line.replace("\n","").replace(" ","").replace("\t","")
		words.add(line)

# Process lines of books
for line in sys.stdin:
	# Manage name of file
	file = os.environ['mapreduce_map_input_file']
	prefix, file = file.split("u-")
	line = re.sub('[^a-z ]', ' ', line.lower())
	if file not in book_authors.keys(): continue;

	# Get name of author
	author=book_authors[file]
	# Do not consider author Various and Anonymous
	if author != "Various".lower() and author != "Anonymous".lower():
		if author not in author_words.keys():
			author_words[author] = set()
		for word in line.split() :
			# Count each word once
			if word not in author_words[author]:
				author_words[author].add(word)
				# Check if word is popular or not
				if (word in words):
					print(author + "," + word + ",0")
				else:
					print(author + "," + word + ",1")
