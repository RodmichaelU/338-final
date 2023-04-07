from myLib.datastructures.nodes import Node
from SLL import SLL

class CircularSLL(SLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head:                        
            self.tail.next = self.head      # For CSLL, the next value of tail must be head to maintain circularity
        
    def insert_head(self, node):
        super().insert_head(node)
        self.tail.next = self.head          # To maintain circularity
    
    def insert_tail(self, node):
        super().insert_tail(node)
        self.tail.next = self.head          # To maintain circularity

    def insert(self, node, index):
        super().insert(node, index)
        if index == 0:
            self.tail.next = self.head      # If its inserted into first value, we must change tail node to point to the head node now

    def delete_head(self):
        if self.head == self.tail:          # If only one node is present
            self.tail = None
        super().delete_head()
        if self.head:                       # If we don't have an empty CSLL, maintain circularity
            self.tail.next = self.head

    def delete_tail(self):
        super().delete_tail()
        if self.tail:                       # Maintain circularity, next of tail node now points to head
            self.tail.next = self.head

    def delete(self, data):
        if self.head is None:                           # Cannot delete from empty list, raise an error
            raise RuntimeError("Cannot Delete From an Empty List")
        
        if self.head and self.head.data == data:
            self.delete_head()                          # If data is at head node, undergo normal head deletion
            return
       
        current = self.head
        index = 0
        while current.next.data != data and index < self.size:       # Find Node with data, or until we iterate to end of linked list
            current = current.next
            index += 1                                                                                                              

        if index == self.size:                                        # Means we iterate through entire list
            raise ValueError("Node Not Found")

        if index == self.size - 1:                                    # The case of tail deltion, desired node is tail node
            self.delete_tail()
            return

        current.next = current.next.next                              # Set the Node next to the next of the next node            
        self.size -= 1
    
    def clear(self):
        super().clear()
    
    def print(self):
        super().print()
        if self.head:                                                  # Show the circularity, and next value of the tail node
            print("Tail next: ", self.tail.next.data)