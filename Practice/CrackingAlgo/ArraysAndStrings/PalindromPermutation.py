#!/usr/bin/env python3

# Palindrome Permutation: Given a string, write a function to check if it is a
# permutation of a palin- drome. A palindrome is a word or phrase that is the
# same forwards and backwards. A permutation is a rearrangement of letters.
# The palindrome does not need to be limited to just dictionary words.

# EXAMPLE
# Input: Tact Coa
# Output: True (permutations: "taco cat". "atco cta". etc.)

# Hints:
# 106: You do not have to-and should not-generate all permutations.This would be very inefficient.
# 121: What characteristics would a string that is a permutation of a palindrome have?
# 134: Have you tried a hash table? You should be able to get this down to 0 (N) time.
# 136: Can you reduce the space usage by using a bit vector?


def palindrome_permutation(string):
    dictionary = dict()
    print(string)
    string = string.replace(' ', '')
    string = string.lower()
    for char in string:
        if char not in dictionary:
            dictionary[char] = 1
        else:
            dictionary[char] += 1

    dictionaryLength = len(dictionary)
    countOdd = 0
    for value in dictionary.values():
        if value % 2 != 0:
            countOdd += 1

    if countOdd > 1:
        return False
    return True


def isPalindrome(string):
    halfLength = int(len(string)/2)
    charList = list(string)
    for i in range(0, halfLength):
        if (charList[i] != charList[len(string) - i - 1]):
            return False

    return True


if __name__ == '__main__':
    string = input()
    print(palindrome_permutation(string))
