#!/usr/bin/env python3

# String Rotation: Assume you have a method isSubstring which checks if one word is a substring of another.
# Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one call
# to isSubstring (e.g.,"waterbottle"is a rotation of"erbottlewat").


def isSubstring(s1, s2):
    ''' if s2 is a substrinng of s1s1, it is also the rotation of s1 '''
    if(len(s1) != len(s2)):
        return False

    temp = s1 + s1

    # count the number of occurrence of s2 in temp
    if(temp.count(s2) > 0):
        return True

    return False


if __name__ == '__main__':
    s1 = input()
    s2 = input()
    print(isSubstring(s1, s2))
