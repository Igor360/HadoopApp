#!/usr/bin/python

import sys
import operator

print("Month | \t Medium temperature")

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        # Something has gone wrong
        continue
    thisMonth, thisSum, thisDays = data_mapped
    print("{0}\tz{1}".format(thisMonth, thisSum / thisDays))
