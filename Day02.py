__author__ = 'Wilro - https://github.com/SciWilro'
# --------------------------------------------------------------------------- #
# Day 2 - #AdventOfCode2022
# --------------------------------------------------------------------------- #
from os import path
inputpath = path.relpath("input/D02_input.txt")
# --------------------------------------------------------------------------- #

# A for Rock, B for Paper, and C for Scissors
# X for Rock, Y for Paper, and Z for Scissors
# --------------------------------------------------------------------------- #

def convertmove(m2: str) -> str:
    if m2 == 'X':
        return 'A'
    elif m2 == 'Y':
        return 'B'
    return 'C'
 
# A for Rock, B for Paper, and C for Scissors
def get_outcome(m1: str, m2: str) -> int:
    score = 0
    if m1 == m2:
        score = 3
    if m1 == 'A':
        if m2 == 'B':
            score = 6
        if m2 == 'C':
            score = 0
    if m1 == 'B':
        if m2 == 'C':
            score = 6
        if m2 == 'A':
            score = 0
    if m1 == 'C':
        if m2 == 'A':
            score = 6
        if m2 == 'B':
            score = 0
    return score + getshape(m2)

def getshape(m2: str) -> int:
    if m2 == 'A':
        return 1
    if m2 == 'B':
        return 2
    if m2 == 'C':
        return 3

scores = []
with open(inputpath) as f:
    for line in f:
        m1, m2 = line.strip().split(' ')
        scores.append(get_outcome(m1,convertmove(m2)))
print(f"score: {sum(scores)}")

# --------------------------------------------------------------------------- #
# --------------------------------------------------------------------------- #
# X = Lose, Y = Draw, Z = Win
# A for Rock, B for Paper, and C for Scissors
def get_move(m1: str, res: str) -> str:
    if res == 'Y':
        return m1
    if res == 'X': # Lose
        if m1 == 'A':
            return 'C'
        if m1 == 'B':
            return 'A'
        if m1 == 'C':
            return 'B'
    if res == 'Z': # Win
        if m1 == 'A':
            return 'B'
        if m1 == 'B':
            return 'C'
        if m1 == 'C':
            return 'A'


scores = []
with open(inputpath) as f:
    for line in f:
        m1, res = line.strip().split(' ')
        print(m1)
        print(res)
        scores.append(get_outcome(m1,get_move(m1,res)))
print(f"score: {sum(scores)}")

# Shorter Alternative
# Hardcode answers in list/dict
lines = [line.strip() for line in open(inputpath).readlines()]
answers = {"A X": 3, "A Y": 4, "A Z": 8, "B X": 1, "B Y": 5, "B Z": 9, "C X": 2, "C Y": 6, "C Z": 7}
print(f"Score For Part 2: {sum(answers[i] for i in lines)}")

# "Better" Alternative
# Convert to numbers (Modular Arithmetic)
# https://www.youtube.com/watch?v=lNFMyI3JBeY