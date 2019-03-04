#!/usr/bin/python3

# URLify: Write a method to replace all spaces in a string with '%20:
# You may assume that the string has sufficient space at the end to hold the additional characters,
# and that you are given the "true" length of the string. (Note: If implementing in Java, please use
# a character array so that you can perform this operation in place.)

# EXAMPLE
# Input: "Mr John Smith ", 13 Output: "Mr%20J ohn%20Smith"


def URLify(string, length):
    # string = string.replace(' ', '%20')
    counter = 0
    string = list(string)

    for char in string:
        if counter < length and char == ' ':
            string[counter] = '%20'
        counter += 1
    string = ''.join(string)

    return string


if __name__ == '__main__':
    string = input()
    length = input()
    print(URLify(string, int(length)))
