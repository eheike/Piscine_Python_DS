#!/bin/sh
OUTPUT_FILE="./hh.json"
JQ="/Users/eheike/Desktop/homebrew/bin/jq"
curl -A "chasimir" -G "https://api.hh.ru/vacancies"\
  --data-urlencode "text=${1}"\
  --data-urlencode 'page=0'\
  --data-urlencode 'per_page=20'\
  | $JQ > hh.json