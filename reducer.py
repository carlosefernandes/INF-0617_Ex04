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

for line in sorted_counts :
    if (lines_counter < 3000):
        print(line[0])
        lines_counter = lines_counter + 1
    else:
        break;
