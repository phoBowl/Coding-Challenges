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
    ''' Method 1: using dictionary - if temporary buffer is allowed  O(N)'''
    dictionary = dict()
    curr = llist.getHead()

    if curr == None:
        return llist

    prevNode = Node()
    while(curr):
        curr_val = curr.getValue()
        if curr_val not in dictionary:
            dictionary[curr_val] = 1
            prevNode = curr
        else:
            if curr_val in dictionary:
                prevNode._next = curr.getNextNode()
                llist._size -= 1
        curr = curr.getNextNode()
    return llist


def removeDups2(llist):
    ''' Method 2: Linked List tranversal -  temporary buffer is not allowed  O(n^2)'''
    curr = llist.getHead()

    if(curr == None):
        return llist

    while(curr != None):
        temp_node = curr
        while(temp_node.getNextNode() != None):
            if temp_node.getNextNode().getValue() == curr.getValue():
                if temp_node.getNextNode().getNextNode() != None:
                    temp_node._next = temp_node._next._next
                    llist._size -= 1
                else:
                    temp_node._next = None
                    break
            temp_node = temp_node.getNextNode()
        curr = curr.getNextNode()

    return llist
