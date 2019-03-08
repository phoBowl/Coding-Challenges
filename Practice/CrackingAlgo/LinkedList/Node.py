class Node:
    def __init__(self, value=None, nextNode=None):
        self._value = value
        self._next = None

    def getValue(self):
        return self._value

    def setValue(self, value):
        self._value = value

    def getNextNode(self):
        return self._next

    def setNextNode(self, value):
        self._next.value = value

    def appendToTail(self, value):
        newNode = Node(value)
        n = self
        while n.getNextNode() != None:
            n = n.getNextNode()
        n._next = newNode


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
