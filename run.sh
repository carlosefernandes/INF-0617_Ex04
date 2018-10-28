#!/bin/bash
#CONFIGURATION PATHS
WORK_FOLDER=/tmp/data/INF-0617_Ex04
INPUT_FOLDER=/tmp/data/books/txt
INPUT_INDEX=/tmp/data/books/master_list.csv

#INITIALIZATION
OUT_FOLDER=/tmp/data/INF-0617_Ex04/output
rm -rf $OUT_FOLDER

#PART-I
$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input $INPUT_FOLDER/ \
-output $OUT_FOLDER/out1 \
-mapper "python $WORK_FOLDER/map.py" \
-reducer "python $WORK_FOLDER/reducer.py"

#Case there is more than one reducer - 
# we should treat the 3000 file selection here
cat $OUT_FOLDER/out1/* >$OUT_FOLDER/index.txt 

#PART-II
$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input $INPUT_FOLDER/ \
-output $OUT_FOLDER/out2 \
-mapper "python $WORK_FOLDER/map_2.py $INPUT_INDEX $OUT_FOLDER/index.txt" \
-reducer "python $WORK_FOLDER/reducer_2.py"

cat $OUT_FOLDER/out2/*