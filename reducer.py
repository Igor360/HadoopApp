#!/usr/bin/python

import sys
import operator

print("Month | \t Medium temperature")

lines = sys.stdin
next(lines)

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 3:
        # Something has gone wrong
        continue
    thisMonth, thisSum, thisDays = data_mapped
    mediumTemp = float(thisSum) / int(thisDays)
    print("{0}\t{1}".format(thisMonth, mediumTemp))
