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

To do so, we use a Mapreduce strategy that maps `Map(Key,Value)` all words to {Author, Word} tuples. The idea is to ignor the book names so every word within a book is associated with a specific author.

On the reducer side we create a dictionary for each author. For each tuple that arrives we add the word to its author dictionary if not already exist. By the end of this process we have 


Our reducer strategy is to combine all keys (party number) by summing their values (number of votes). Shuffeling would try to direct the same key to the same reducer worker. However, even if two workers were summing the same key, they can later be reduced by this same strategy.

### Results:
Here we show the finnel results of our program. Remembering that the 95 party code was converted to blank vote and 96 as Null vote. There were no 97 ("Voto Anulado e Apurado em Separado") party codes in the database:

	13 - 3888584	
	15 - 4594708	
	21 - 12958	
	28 - 22822	
	29 - 11118	
	31 - 132042	
	43 - 260696	
	45 - 12230807	
	50 - 187487	
	Voto Branco - 2020613	
	Voto Nulo - 2374946	
