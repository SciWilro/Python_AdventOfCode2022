__author__ = 'Wilro - https://github.com/SciWilro'
# --------------------------------------------------------------------------- #
# Day 3 - #AdventOfCode2022
# --------------------------------------------------------------------------- #
from os import path
inputpath = path.relpath("input/D03_input.txt")
# --------------------------------------------------------------------------- #

# Helper Function
def get_priority(s: str) -> int:
    if s.islower():
        return ord(s)-96
    else:
        return ord(s)-38

dups = []
with open(inputpath) as f:
    for line in f:
        w1, w2 = line[:len(line)//2], line[len(line)//2:]
        dups.append(''.join(set(w1).intersection(w2)))

# Answer 1
sum(get_priority(i) for i in dups)

# --------------------------------------------------------------------------- #

bags = [line.strip() for line in open(inputpath).readlines()]
dups = []

for i in range(0, len(bags), 3):
    dups.append(''.join(set(bags[i]).intersection(bags[i+1], bags[i+2])))

# Answer 2
sum(get_priority(i) for i in dups)
