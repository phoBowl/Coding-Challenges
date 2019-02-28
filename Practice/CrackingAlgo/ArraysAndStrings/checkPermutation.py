#!/usr/bin/python3

# Check Permutation: Given two strings, write a method to decide if one is a permutation of the other.


def checkPermutation(str1, str2):
    dictionary = dict()
    for char in str1:
        if char not in dictionary:
            dictionary[char] = char

    for char in str2:
        if char not in dictionary:
            return False

    return True


if __name__ == '__main__':
    string1 = input()
    string2 = input()
    print(checkPermutation(string1, string2))
