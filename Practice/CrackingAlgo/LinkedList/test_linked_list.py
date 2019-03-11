
import pytest
from LinkedList import LinkedList


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
