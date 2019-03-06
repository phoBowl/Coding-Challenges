#!/usr/bin/env python3


# String Compression: Implement a method to perform basic string compression using the
# counts of repeated characters.
# For example, the string aabcccccaaa would become a2b1c5a3.
# If the "compressed" string would not become smaller than the original string,
# your method should return the original string.
# You can assume the string has only uppercase and lowercase letters (a - z).
# Hints: #92, # 110

def stringCompression(string):
    counter = 0
    newList = list()

    tempChar = string[0]

    i = 0
    while i < len(string):
        if tempChar == string[i]:
            counter += 1
            tempChar == string[i]
        elif tempChar != string[i]:
            newList.append(tempChar)
            newList.append(str(counter))
            counter = 1
            tempChar = string[i]

        i += 1

    # append last character
    newList.append(tempChar)
    newList.append(str(counter))

    return ''.join(newList)


if __name__ == '__main__':
    string = input()
    print(stringCompression(string))
