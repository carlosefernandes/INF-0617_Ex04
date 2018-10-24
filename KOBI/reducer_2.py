import sys

authors = {}
authors_score = {}
ordered = {}
for line in sys.stdin:
	author, word, value = line.split(',')
	if author not in authors.keys():
		authors[author] = []
		authors_score[author] = [0,0]
		ordered[author] = 0
	if word not in authors[author]:
		authors[author].append(word)
		authors_score[author][0]+=1
		authors_score[author][1]+=float(value)

for author in authors.keys():
	ordered[author] = authors_score[author][1]/authors_score[author][0]
	
final_result = [(k, ordered[k]) for k in sorted(ordered, key=ordered.get, reverse=True)]
for result in final_result:
	print(result[0] + ", " + str(result[1]))