#!/usr/bin/python3

# Is Unique: Implement an algorithm to determine if a string has all unique characters.
# What if you cannot use additional data structures?
# Can you solve it in O(N log N) time? What might a solution like that look like?

# O(N)


def isUnique(str):
    dictionary = dict()

    for char in str:
        if char not in dictionary:
            dictionary[char] = 0
        else:
            dictionary[char] += 1

    for key in dictionary:
        if dictionary[key] > 0:
            return False
    return True


if __name__ == "__main__":
    inputString = input()
    print(isUnique(inputString))
