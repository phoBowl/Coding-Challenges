from LinkedList import LinkedList
from Node import Node

if __name__ == '__main__':
    myList = LinkedList()
    myList.addNewNode(1)
    myList.appendToTail(2)
    myList.appendToTail(3)
    myList.appendToTail(4)
    myList.appendToTail(5)

    myList.printNodes()
