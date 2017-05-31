#!/bin/bash

time hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-2.7.3*.jar \
-file /home/hduser/mapper.py    -mapper /home/hduser/mapper.py \
-file /home/hduser/reducer.py   -reducer /home/hduser/reducer.py \
-input /user/million/all.txt -output /user/million/outputresults2 |& tee runlog.txt
