#!/usr/bin/python
"""
`reducer.py` reads the output of `mapper.py` from STDIN and sums the occurrences of every word. The counts are written
to STDOUT. Assumes input words are sorted.
"""

import sys

word = ""
current_word = ""
current_count = 0
current_doc_id = ""

for line in sys.stdin:
    line = line.strip()
    word, count, doc_id = line.split("\t")

    if not current_doc_id or doc_id != current_doc_id:
        current_doc_id = doc_id
    try:
        count = int(count)
    except ValueError:
        continue
    if current_word == word:
        current_count += count
    else:
        if current_word:
            print(f"(({current_word}, {current_doc_id}) {current_count})")
        current_word = word
        current_count = count
if current_word == word:
    print(f"(({current_word}, {current_doc_id}) {current_count})")
