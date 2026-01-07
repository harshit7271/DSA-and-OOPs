class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head

    # Insertion at the end of a singly Linked List
    def insertAtEnd(self, value):
        temp_node = Node(value)
        if (self.head != None):
            t1 = self.head  # Now we will tarverse t1 forward
            while (t1.next != None):
                t1 = t1.next
            t1.next = temp_node
        else:
            self.head = temp_node   # means when the first node contain Null value itself

    # Insertion at the begining of a singly Linked List
    def insertAtBegining(self, value):
        temp_node = Node(value)
        temp_node.next = self.head
        self.head = temp_node

    def printLinkedList(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SinglyLinkedList()

obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtBegining(5)
obj.insertAtEnd(30)
obj.printLinkedList()
