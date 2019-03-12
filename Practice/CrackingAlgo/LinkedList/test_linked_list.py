
import pytest
from LinkedList import LinkedList
from removeDups import *


def test_append_to_tail():
    llist = LinkedList()
    llist.appendToTail(1)

    assert llist.getSize() == 1

    llist.appendToTail(2)

    assert llist.getHead().getValue() == 1
    assert llist.getSize() == 2


def test_add_new_node():
    llist = LinkedList()
    llist.addNewNode(5)

    assert llist.getHead().getValue() == 5

    llist.addNewNode(2)

    assert llist.getHead().getValue() == 2
    assert llist.getHead().getNextNode().getValue() == 5

    llist.addNewNode(3)

    assert llist.getHead().getValue() == 3
    assert llist.getHead().getNextNode().getValue() == 2
    assert llist.getHead().getNextNode().getNextNode().getValue() == 5


def test_delete_node():
    llist = LinkedList()
    llist.appendToTail(1)
    llist.appendToTail(2)
    llist.appendToTail(3)
    llist.appendToTail(4)
    llist.appendToTail(5)
    llist.addNewNode(10)

    assert llist.getSize() == 6
    assert llist.getHead().getValue() == 10

    llist.deleteNode(2)

    assert llist.getSize() == 5
    assert llist.getHead().getValue() == 10  # head still the same

    llist.deleteNode(10)  # delete head
    assert llist.getHead().getValue() == 1  # change head to the next node
    assert llist.getHead().getNextNode().getValue() == 3  # node 2 is deleted above


def test_delete_node_at_index():
    llist = LinkedList()
    # 2 6 7 1 9 1 2 5 3
    llist.appendToTail(2)
    llist.appendToTail(6)
    llist.appendToTail(7)
    llist.appendToTail(1)
    llist.appendToTail(9)
    llist.appendToTail(1)
    llist.appendToTail(2)
    llist.appendToTail(5)
    llist.appendToTail(3)

    assert llist.getSize() == 9

    llist.deleteNodeAt(2)
    assert llist.getSize() == 8

    llist.deleteNodeAt(2)
    assert llist.getSize() == 7

    llist.deleteNodeAt(0)
    assert llist.getSize() == 6
    assert llist.getHead().getValue() == 6
    assert llist.getHead().getNextNode().getValue() == 9


def test_remove_duplicate1():
    ''' using dictionary - if temporary buffer is allowed '''
    llist = LinkedList()
    # 2 6 7 1 9 1 2 5 3
    llist.appendToTail(2)
    llist.appendToTail(6)
    llist.appendToTail(7)
    llist.appendToTail(1)
    llist.appendToTail(9)
    llist.appendToTail(1)
    llist.appendToTail(2)
    llist.appendToTail(5)
    llist.appendToTail(3)

    assert llist.countOccurence(2) == 2
    assert llist.countOccurence(6) == 1
    assert llist.countOccurence(7) == 1
    assert llist.countOccurence(1) == 2

    llist = removeDups1(llist)
    assert llist.getSize() == 7
    assert llist.countOccurence(2) == 1
    assert llist.countOccurence(1) == 1
    assert llist.getHead().getValue() == 2
    assert llist.getHead().getNextNode().getValue() == 6


def test_remove_duplicate2():
    ''' no buffer allowed '''
    llist = LinkedList()
    # 2 6 7 1 9 1 2 5 3
    llist.appendToTail(2)
    llist.appendToTail(6)
    llist.appendToTail(7)
    llist.appendToTail(1)
    llist.appendToTail(9)
    llist.appendToTail(1)
    llist.appendToTail(2)
    llist.appendToTail(5)
    llist.appendToTail(3)

    assert llist.countOccurence(2) == 2
    assert llist.countOccurence(6) == 1
    assert llist.countOccurence(7) == 1
    assert llist.countOccurence(1) == 2

    llist = removeDups2(llist)
    assert llist.getSize() == 7
    assert llist.countOccurence(2) == 1
    assert llist.countOccurence(1) == 1
    assert llist.getHead().getValue() == 2
    assert llist.getHead().getNextNode().getValue() == 6
