# INF-0617: Ex04, Vocaulary Complexity
## Students: Carlos Eduardo Fernandes and Yakov Nae 

In this exercise we will be working with the Gutenberg library that contains 595 files, hostinga total space of 427MB. Our goal is to determine who is the most complex author. In other words, we the portion of exotic words evry author is using and select the one with the highest relation between exotic and regular words.

### Running instructions:
This zip file contains a run.sh file with the following three fields:

	#CONFIGURATION PATHS
	WORK_FOLDER=/tmp/data/INF-0617_Ex04/KOBI
	INPUT_FOLDER=/tmp/data/books/txt_tst
	INPUT_INDEX=/tmp/data/books/master_list.csv
	
In order to run our code, please modify these three reference accordingly. The `WORK_FOLDER` variable is where our code is at. Also, output files will be writen to this folder. The `INPUT_FOLDER` variable is the folder where the Gutenberg *.txt files is at within the container. `INPUT_INDEX` is where the index file is (book file -> author name). After modifing these variables, please execute `$ ./run.sh`.

Our solution is consisted of two parts:

### Part-I finding the 3000 most used words
On the first part our problem is a classical map reduce problem. We would like to count the occurances of each word within all files from the Gutenberg library. To do so, we use a map function `Map(key,value)` for every word in every file of the Gutenberg library.

Shuffeling willdirect same words to the same reducer so we can count their overall apearences. Then, we order the word list and print the 3000 most used words to the result folder.
 
### Part-II Calculating the complexity factor of each author
In this part we have two tasks. The first is to determine the words list associated with each author. The second is to calculate the portion of words that not appear in the list from part-I and divide them by the author words list size.

To do so, we use a Mapreduce strategy that maps `Map(Key,Value)` all words to {Author, Word} tuples. The idea is to ignor the book names so every word within a book is associated with a specific author. Moreover, we load the index file with the 3000 most common words and for each tuple we verify if its value (Word) is an exotic or normal word. Therefore, our map is actually transmitting 2 valeus per key: `Map(Key, v1, v2)` where our key is the author name, v1 is the actual word and v2 is 0 for a normal word and 1 for an exotic word. The reason we chose 0 and 1 is related with the reducer part.

The shuffel here sends same author triples to the same reducer. If the word doesn't exist in the suthor dictionary, we will insert it and sum both the dictionary size and the complexity coeficient (summing 1 for exotic word and 0 for a regular one). In the end we order this list, created by the reducer and transmit it. 
###Results