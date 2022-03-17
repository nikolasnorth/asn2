#!/usr/bin/python
"""
`mapper.py` reads data from STDIN, splits it into words, and outputs a list of lines mapping words to their
(intermediate) counts to STDOUT. However, it will not compute a sum of the word's occurrences. The reducer script will
do the final sum count.
"""
import sys

current_doc_id = ""

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    if len(words) == 2 and words[0] == "ID":
        current_doc_id = words[1]
        continue
    for word in words:
        print(f"{word}\t1\t{current_doc_id}")
