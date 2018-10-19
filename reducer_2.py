import sys

authors = {}

for line in sys.stdin:
	author, word, value = line.split(',')
	if author not in authors.keys():
		authors[author] = {}
		authors[author][word] = value
	else:
		if word not in authors[author].keys():
			authors[author][word] = value.replace("\n","").strip()

ordered = {}

for author in authors.keys():
	counter = 0
	exotics = 0
	for word in authors[author]:
		counter = counter + 1
		if authors[author][word] == '1':
			exotics = exotics + 1
	ordered[author] = exotics/counter


final_result = [(k, ordered[k]) for k in sorted(ordered, key=ordered.get, reverse=True)]

for result in final_result:
	print(result[0] + " " + str(result[1]))