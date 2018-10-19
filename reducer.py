import sys
import operator

counts = {}

for line in sys.stdin:
    word, count = line.split(',')
    count = int(count)
    if word not in counts :
        counts[word] = count
    else :
        counts[word] = counts[word] + count

sorted_counts = sorted(counts.items(),key = operator.itemgetter(1),reverse = True)

lines_counter = 0

index_file = open("index.txt","w") 

for line in sorted_counts :
    if (lines_counter < 3000):
        index_file.write(line[0] + "\n")
        lines_counter = lines_counter + 1
    else:
        break;

index_file.close()