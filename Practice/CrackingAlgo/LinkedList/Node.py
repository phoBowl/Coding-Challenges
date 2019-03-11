# Singly Linked List
class Node:
    def __init__(self, value=None, nextNode=None):
        self._value = value
        self._next = nextNode

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def getNextNode(self):
        return self._next

    def setNextNode(self, newnode):
        self._next = newnode
