#!/bin/sh
INPUT_FILE=../ex01/hh.csv
OUTPUT_FILE=hh_sorted.csv 
head -n 1 $INPUT_FILE > $OUTPUT_FILE
tail -n +2 $INPUT_FILE | sort -nk2 | sort -nk1 >> $OUTPUT_FILE