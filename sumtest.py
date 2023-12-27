#!/usr/bin/python3

"""
Programm to compare sha256 sums.
This Program takes 2 inputs: First file to hash and second the checksum from webpage.
Script must be used in the folder where the file is placed.
"""

import sys
import hashlib
import os


class Colors:
    """Color Class for ASCII Terminal"""
    green = "\033[0;32m"
    red = "\033[0;31m"
    end = "\033[00m"


to_sum = sys.argv[1]

comp_sum = sys.argv[2]


def main(to_sum, comp_sum):
    to_sum_file = os.path.join(os.curdir, to_sum)

    print("\nDie Datei die getestet wird: ")
    print(to_sum_file + "\n")

    with open(to_sum_file, "rb") as f:
        is_sum = hashlib.sha256(f.read())

    print("Der erstellte sha256 Haswert: ")
    print(is_sum.hexdigest() + "\n")

    if is_sum.hexdigest() == comp_sum:
        print(f"\n{Colors.green}Hashwerte sind identisch!!!{Colors.end}")
    else:
        print(f"\n{Colors.red}Hashes stimmen nicht überein!!!{Colors.end}")


main(to_sum, comp_sum)
