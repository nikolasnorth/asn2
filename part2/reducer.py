#!/usr/bin/python
"""
`reducer.py` reads the output of `mapper.py` from STDIN and sums the occurrences of every two-word combination.
"""
import sys

current_word_1, current_word_2, current_count = "", "", 0
for line in sys.stdin:
    line = line.strip()
    word1, word2, count = line.split("\t")
    try:
        count = int(count)
    except ValueError:
        continue
    if not current_word_1 and not current_word_2:
        current_word_1, current_word_2, current_count = word1, word2, count
        continue
    if word1 == current_word_1 and word2 == current_word_2:
        current_count += 1
    elif word1 == current_word_1:
        print(f"(({current_word_1}, {current_word_2}), {current_count})")
        current_word_2, current_count = word2, count
    else:
        print(f"(({current_word_1}, {current_word_2}), {current_count})")
        current_word_1, current_word_2, current_count = word1, word2, count
print(f"(({current_word_1}, {current_word_2}), {current_count})")
