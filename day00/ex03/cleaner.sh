#!/bin/sh
head -n 1 ../ex02/hh_sorted.csv > hh_positions.csv
tail -n +2 ../ex02/hh_sorted.csv | \
awk 'BEGIN { FS = OFS = "," } 
    {
        STR = ""
        if (tolower($3) ~ "middle")
        {
            if (tolower($3) ~ "junior" && tolower($3) ~ "senior")
                STR = "Junior/Middle/Senior"
            else if (tolower($3) ~ "junior")
               STR = "Junior/Middle"
            else if (tolower($3) ~ "senior")
                STR = "Middle/Senior"
            else
                STR = "Middle"
        }
        else if (tolower($3) ~ "junior")
            STR = "Junior"
        else if (tolower($3) ~ "senior")
            STR = "Senior"
        else
            STR = "-"
        $3 = "\""STR"\""
        print
    }' >> hh_positions.csv