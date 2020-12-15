#!/usr/bin/python

import sys
import csv
from datetime import datetime

reader = csv.DictReader(sys.stdin, delimiter=',')
next(reader)

firstDay = None
FMT = "%d.%m.%Y %H:%M"

sumTemp = 0
days = 0

for line in reader:
    days = (firstDay - datetime.strptime(line['LocalTime'], FMT)).days if firstDay is not None else 0
    if firstDay is None or days >= 30:
        print("{0}\t{1}\t{2}".format(firstDay, sumTemp, days))
        firstDay = datetime.strptime(line['LocalTime'], FMT)
        sumTemp = 0
    sumTemp += float(line['T']) if '' != line['T'] else 0
