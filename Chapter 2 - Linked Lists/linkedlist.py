class Node:
    '''
    The Node class of the LinkedList
    '''
    def __init__(self):
        self.data = None # contains the data
        self.next = None # contains the reference to the next node


class linkedList:
    def __init__(self):
        self.currentNode = None

    def addNode(self, data):
        '''
        Add a Node to the LinkedList
        :param data: the data to be entered to the list
        '''
        newNode = Node()               # create a new node
        newNode.data = data
        newNode.next = self.currentNode   # link the new node to the 'previous' node.
        self.currentNode = newNode        #  set the current node to the new one.

    def removeNode(self, location):
        '''
        Remove a Node from the LinkedList
        :param head: The previous position
        :param next: The next value of the linkedlist
        '''
        node = self.currentNode
        count = 0
        while count != location:
            node = node.next
            count += 1
        node.next = node.next.next

    def printList(self):
        '''
        Prints the LinkedList
        '''
        node = self.currentNode            #  cant point to ll!
        while node:
            print(node.data)
            node = node.next

ll = linkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.removeNode(2)

ll.printList()