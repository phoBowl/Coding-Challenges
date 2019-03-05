#!/usr/bin/env python3


# String Compression: Implement a method to perform basic string compression using the
# counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, # 110

# def stringCompression(string):
#     dictionary = dict()
#     for char in string:
#         if char not in dictionary:
#             dictionary[char] = 1
#         else:
#             dictionary[char] += 1

#     compressedString = ''
#     for key in dictionary:
#         compressedString += key
#         compressedString += (str(dictionary[key]))

#     return compressedString

def stringCompression(string):
    newString = ''
    counter = 0

    tempChar = string[0]
    for char in string:


if __name__ == '__main__':
    string = input()
    print(stringCompression(string))
