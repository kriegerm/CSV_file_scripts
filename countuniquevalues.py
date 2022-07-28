#!/usr/bin/env python3

'''
countuniquevalues.py

This simple script takes in a single column csv file with a bunch of values
and returns a csv file with tallys of the unique values in the at original csv.
'''

import csv
import sys

def count(inputcsv, outputcsv):

    uniquematchdict = {}

    with open(inputcsv, "r") as fh:
        fhcsv = csv.reader(fh, delimiter=',')

        for line in fhcsv:
            entry = line[0]

            if entry in uniquematchdict:
                uniquematchdict[entry] += 1
            else:
                uniquematchdict[entry] = 1

    print(uniquematchdict)

    with open(outputcsv, 'w') as fh:
        writer = csv.writer(fh)
        for key, value in uniquematchdict.items():
            writer.writerow([key, value])

if __name__ == '__main__':
    if len(sys.argv) == 3:
         count(sys.argv[1], sys.argv[2])
    else:
         print("Usage: countuniquevalues.py input.csv output.csv")
         sys.exit(0)
