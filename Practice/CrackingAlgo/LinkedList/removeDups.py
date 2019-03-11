#!/usr/bin/env python3

from LinkedList import LinkedList
from Node import Node

# Remove Dups: Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?
# Hints:
# 9: Have you tried a hash table? You should be able to do this in a single pass of the linked list
# 40: Without extra space, you'll need a(N2) time. Try using two pointers, where the second
#     one searches ahead of the first one.


def removeDups1(llist):
    ''' Method 1: using dictionary - if temporary buffer is allowed '''
    dictionary = dict()
    curr = llist.getHead()

    if curr == None:
        return llist

    while(curr):
        curr_val = curr.getValue()
        if curr_val not in dictionary:
            dictionary[curr_val] = 1
        else:
            if curr_val in dictionary:
                dictionary[curr_val] += 1
                if dictionary[curr_val] > 1:
                    dictionary
        curr = curr.getNextNode()

        # not done yet


def removeDups2(llist):
    ''' Method 2: Linked List tranversal -  temporary buffer is not allowed '''
    pass
