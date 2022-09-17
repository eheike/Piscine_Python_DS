#!bin/sh
FILE=../ex00/hh.json
JQ="/Users/eheike/Desktop/homebrew/bin/jq"
$JQ -rf filter.jq $FILE > hh.csv