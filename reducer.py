#!/usr/bin/python
"""
`reducer.py` reads the output of `mapper.py` from STDIN and sums the occurrences of every word. The counts are written
to STDOUT.
"""

import sys

current_word = ""
current_count = 0
word = ""

for line in sys.stdin:
    # Remove leading and trailing whitespace
    line = line.strip()
    # Parse the current line
    word, count = line.split("\t")
    try:
        count = int(count)
    except ValueError:
        # Skip
        continue
    # Since Hadoop sorts map output by key (i.e. `word`) before it is passed to the reducer, we are able to use an
    # if condition here.
    if current_word == word:
        current_count += count
    else:
        if current_word:
            # Write result to STDOUT
            print(f"{current_word}\t{current_count}")
        current_word = word
        current_count = count
# Output the last word
if current_word == word:
    print(f"{current_word}\t{current_count}")
