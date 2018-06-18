#!/usr/bin/env python

from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()
    word , count = line.split('\t', 1)

    try:
        count = int(count)
    except ValueError:
        continue

    if(current_word == word):
        current_count += count
    else:
        if(current_word):
            print("{0}\t{1}".format(current_word,current_count))
        current_word = word
        current_count = count
if(current_word == word):
    print("{0}\t{1}".format(current_word,current_count))
