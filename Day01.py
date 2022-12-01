__author__ = 'Wilro - https://github.com/SciWilro'
# --------------------------------------------------------------------------- #
# Day 1 - #AdventOfCode2022
# --------------------------------------------------------------------------- #
from os import path
inputpath = path.relpath("input/D01_input.txt")
# --------------------------------------------------------------------------- #

with open(inputpath) as f:
    max, total = [], 0
    for line in f:
        if line == '\n':
            max.append(total)
            total = 0
        else:
            total += int(line)

print(f"The Elf we are looking for in Problem 1 has {sorted(max)[-1]} calories")
print(f"The top 3 for Problem 2 we are looking for has a total of {sum(sorted(max)[-3:])} calories")

# <Done>

# --------------------------------------------------------------------------- #
# Problem 1 - Slower method (But using something new I learnt)
# --------------------------------------------------------------------------- #
with open(inputpath) as f:
    max = total = 0
    for line in f:
        if line == '\n':
            total = 0
        else:
            total += int(line)
        max = (max, total)[total > max] # # Shorthand ternary operator: (<OnFalse>, <OnTrue>)[<Condition>]
print(f"The Elf we are looking for has {max} calories")
# --------------------------------------------------------------------------- #
# Tuple syntax for ternary operators:
# https://blog.finxter.com/python-ternary-tuple/


# --------------------------------------------------------------------------- #
# Alternative Solution - Shortest
# --------------------------------------------------------------------------- #

with open(inputpath) as f:
    max = []
    for elf in f.read().split("\n\n"):
        max.append(sum(int(i) for i in elf.split("\n") if i != ''))
max.sort()

print(f"The Elf we are looking for in Problem 1 has {max[-1]} calories")
print(f"The top 3 for Problem 2 we are looking for has a total of {sum(max[-3:])} calories")