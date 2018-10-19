#!/bin/bash

rm -rf index.txt 
rm -rf /tmp/data/output_trabalho4

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/_books/txt/ -output /tmp/data/output_trabalho4 -mapper "python /tmp/data/Trabalho4/map.py" -reducer "python /tmp/data/Trabalho4/reducer.py"

rm -rf /tmp/data/output_trabalho4

$HADOOP_HOME/bin/hadoop  jar $HADOOP_HOME/share/hadoop/tools/lib/hadoop-streaming-3.0.0.jar -input /tmp/data/_books/txt/ -output /tmp/data/output_trabalho4 -mapper "python /tmp/data/Trabalho4/map_2.py" -reducer "python /tmp/data/Trabalho4/reducer_2.py"