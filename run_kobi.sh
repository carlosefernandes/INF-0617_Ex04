#!/bin/bash
WORK_FOLDER=/tmp/data/INF-0617_Ex04/KOBI
OUT_FOLDER=/tmp/data/INF-0617_Ex04/output
INPUT_FOLDER=/tmp/data/books/txt_tst
INPUT_INDEX=/tmp/data/books/master_list.csv

rm -rf $OUT_FOLDER

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input $INPUT_FOLDER/ \
-output $OUT_FOLDER/out1 \
-mapper "python $WORK_FOLDER/map.py" \
-reducer "python $WORK_FOLDER/reducer.py"

cat $OUT_FOLDER/out1/* >$OUT_FOLDER/index.txt 

$HADOOP_HOME/bin/hadoop jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar \
-input $INPUT_FOLDER/ \
-output $OUT_FOLDER/out2 \
-mapper "python $WORK_FOLDER/map_2.py $INPUT_INDEX $OUT_FOLDER/index.txt" \
-reducer "python $WORK_FOLDER/reducer_2.py"

cat $OUT_FOLDER/out2/*