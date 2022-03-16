#!/usr/bin/python
"""
`mapper.py` reads data from STDIN, splits it into words, and outputs a list of lines mapping words to their
(intermediate) counts to STDOUT. However, it will not compute a sum of the word's occurrences. The reducer script will
do the final sum count.
"""

import sys


for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Split the line into words
    words = line.split()
    # Increase counters
    for word in words:
        print(f"{word}\t1")
