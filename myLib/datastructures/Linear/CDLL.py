from myLib.datastructures.nodes import DNode
from DLL import DLL

class CDLL(DLL):
    def __init__(self, head=None):
        super().__init__(head)
        if head:                
            self.head.prev = self.tail          # For CDLL the head node must have a prev pointer to the tail node
            self.tail.next = self.head          # For CDLL also, the tail node must have a next pointer to the head node

    def insert_head(self, node):        
        super().insert_head(node)               # Normal head insertion
        self.head.prev = self.tail              # set head.prev and tail.next to maintain circularity
        self.tail.next = self.head

    def insert_tail(self, node):
        super().insert_tail(node)
        self.head.prev = self.tail              # Maintain reverse circularity
        self.tail.next = self.head              # Maintain forwards circularity

    def insert(self, node, index):
        super().insert(node, index)             # Normal insertion for DLL 
        self.head.prev = self.tail              # Ensure reverse circularity
        self.tail.next = self.head              # Ensure forward circularity

    def sorted_insert(self, node):
        current = self.head
        sorted_status = True

        index = 0
        while index < self.size:                             # Checks if the list is sorted
            if current.data > current.next.data:
                sorted_status = False
                break
            current = current.next
            index += 1

        if not sorted_status:                           # If not list is not sorted, sort the list
            self.sort()
        
        if self.head is None or self.head.data >= node.data:
            self.insert_head(node)
        else:
            current = self.head
            while current.next != self.head and current.next.data < node.data:      # Iterate until we find where data should be inserted
                current = current.next
            node.next = current.next                                                # Line and following 3, to maintain the double linked list manner
            node.prev = current
            current.next = node
            current.next.prev = node
            if current == self.tail:
                self.tail = node
            self.size += 1
            self.tail.next = self.head
            self.head.prev = self.tail
    
    def search(self, data):
        current = self.head
        for element in range(self.size):       # Iterate through the size of the linked list
            if current.data == data:
                return current                  # Return correct value if it is found
            current = current.next
        return None             

    def delete_head(self):                       
        if self.size > 1:                       # Update tail next to point to the node next of the head node
            self.tail.next = self.head.next
        super().delete_head()                   # Normal head deletion after, as tail next pointer is already updated

    def delete_tail(self):                       
        if self.size > 1:                       # Update head prev to point to the node prev of the tail node
            self.head.prev = self.tail.prev
        super().delete_tail()                   # Normal tail deletion after, as head prev pointer is already updated

    def sort(self):
        if self.size <= 1:
            return

        sorted_list = CDLL()
        current = self.head
        for element in range(self.size):                    # Iterate through size of CSLL
            next_node = current.next
            current.next = None
            sorted_list.sorted_insert(current)              # Use sorted insert to put in correct place each time
            current = next_node

        self.head = sorted_list.head                        # Set head pointer to sorted_list head
        self.tail = sorted_list.tail                        # Set tail pointer to sorted_list tail
        self.tail.next = self.head
        self.head.prev = self.tail

    def clear(self):
        super().clear()

    def print(self):
        super().print()
        print(f"Head prev: {self.head.prev.data}")       # Conditionally print head prev
        print(f"Tail next: {self.tail.next.data}")       # Conditionally print head tail

