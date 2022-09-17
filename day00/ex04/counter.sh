#!/bin/sh
INPUT_FILE=../ex03/hh_positions.csv
JUN=0
MID=0
SEN=0
echo "\"name\"","\"count\"" > hh_uniq_positions.csv
(tail -n +2 ../ex03/hh_positions.csv | \
awk 'BEGIN { FS = ","; OFS = "," } 
    {
        if ($3 ~ "Junior")
            JUN += 1
        if ($3 ~ "Middle")
            MID += 1
        if ($3 ~ "Senior")
            SEN += 1
    }
    END { print "\"Junior\"",
                JUN "\n\"Middle\"", 
                MID "\n\"Senior\"", SEN } 
    ') | \
    sort -t',' -nrk2\
    >>  hh_uniq_positions.csv