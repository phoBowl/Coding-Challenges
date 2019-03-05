#!/usr/bin/env python3

import math

# One Away: There are three types of edits that can be performed on strings:
# insert a character, remove a character, or replace a character.
# Given two strings, write a function to check if they are one edit (or zero edits) away.
# 23: Start with the easy thing. Can you check each of the conditions separately?
# 97: What is the relationship between the "insert character" option and the "remove character"
#     option? Do these need to be two separate checks?
# 130: Can you do all three checks in a single pass?


def oneAway(string1, string2):

    if string1 == string2:
        return True

    length1 = len(string1)
    length2 = len(string2)

    i = 0
    j = 0

    countDiff = 0

    while (i < length1 and j < length2):

        if string1[i] != string2[j]:
            if countDiff == 1:
                return False

            if length1 > length2:
                j += 1
            elif length2 > length1:
                i += 1
            else:
                i += 1
                j += 1
            countDiff += 1
        else:
            i += 1
            j += 1

    if i < length1 or j < length2:
        countDiff += 1

    if countDiff == 1:
        return True
    else:
        return False


if __name__ == '__main__':
    string1 = input()
    strinng2 = input()
    print(oneAway(string1, strinng2))
