from Node import Node


class LinkedList:
    def __init__(self, head=None):
        self._head = head  # is Node
        self._size = 0

    def getSize(self):
        return self._size

    def getHead(self):
        return self._head

    def addNewNode(self, value):
        ''' Add new node to the beginning of linked list '''
        newNode = Node(value, self._head)
        self._head = newNode
        self._size += 1

    def appendToTail(self, value):
        newNode = Node(value)
        curr = self._head

        if curr == None:
            self._head = newNode
            self._size += 1
            return self._head

        while curr.getNextNode() != None:
            curr = curr.getNextNode()
        self._size += 1

        curr.setNextNode(newNode)

        return self._head

    def deleteNode(self, value):
        ''' Delete a node with given value '''
        curr = self._head

        # If head has the same value, delete it
        if curr.getValue() == value:
            self._head = curr.getNextNode()
            self._size -= 1
            return self._head

        while curr.getNextNode() != None:
            if curr.getNextNode().getValue() == value:
                if curr._next._next != None:
                    curr.setNextNode(curr.getNextNode().getNextNode())
                else:
                    curr.setNextNode(None)
                    break
            curr = curr.getNextNode()

        self._size -= 1
        return self._head

    def deleteNodeAt(self, index):
        ''' Delete node at a specific given index '''
        counter = 0
        curr = self.getHead()

        if curr == None:
            return None

        # head is the index to delete
        if index == 0:
            self._head = curr.getNextNode()
            self._size -= 1
            return self._head

        while(curr.getNextNode() != None):
            if (counter + 1) == index:
                if curr.getNextNode().getNextNode() != None:
                    curr._next = curr._next._next
                else:
                    curr.setNextNode(None)
                    break
            else:
                curr = curr.getNextNode()
            counter += 1

        # updating size
        self._size -= 1

        return self._head

    def printNodes(self):
        curr = self._head
        while(curr != None):
            print(curr.getValue())
            curr = curr.getNextNode()
        print('size: ', self.getSize())
