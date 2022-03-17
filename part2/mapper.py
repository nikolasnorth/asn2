#!/usr/bin/python
"""
`mapper.py` counts all occurrences of all two-word combinations in a single corpus.
"""
import sys

prev_word = ""

for line in sys.stdin:
    line = line.strip()
    words = line.split()
    for word in words:
        if not prev_word:
            prev_word = word
            continue
        print(f"{prev_word}\t{word}\t1")
        prev_word = word
