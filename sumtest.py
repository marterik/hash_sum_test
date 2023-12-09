#!/usr/bin/python3

"""Programm to compare sha256 sums"""

import sys
import hashlib
import os

to_sum = sys.argv[1]

comp_sum = sys.argv[2]

to_sum_file = os.path.join(os.curdir, to_sum)

print("\nDie Datei die getestet wird: ")
print(to_sum_file + "\n")

with open(to_sum_file, "rb") as f:
    is_sum = hashlib.sha256(f.read())

print("Der erstellte sha256 Haswert: ")
print(is_sum.hexdigest() + "\n")


if is_sum.hexdigest() == comp_sum:
    print("\nHashwerte sind identisch")


#Das ist ein Test