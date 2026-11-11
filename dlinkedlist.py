# Double Linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        #DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #DLL is not empty
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    # Insert at ending
    def insert_at_ending(self, data):
        new_node = Node(data)
        #DLL is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        #DLL is not empty
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    # Insert at specific position
    def insert_at_position(self, position, data):
        if position<0 or position>self.length():
            print("Invalid position")
            return
        if position==0:
            self.insert_at_beginning(data)
            return
        if position==self.length():
            self.insert_at_ending(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position-1):
            current = current.next
        previous_node = current.prev
        new_node.prev=previous_node
        new_node.next=current
        previous_node.next=new_node
        current.prev=new_node
    # Delete at beginning
    def delete_at_beginning(self):
        # Check if DLL is empty
        if self.head is None:
            print("DLL is empty")
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
            return
        self.head=self.head.next
        self.head.prev=None
    # Delete at ending
    def delete_at_ending(self):
        # Check if DLL is empty
        if self.head is None:
            print("DLL is empty")
            return
        if self.head==self.tail:
            self.head=None
            self.tail=None
            return
        self.tail=self.tail.prev
        self.tail.next=None
    #delete at specific position
    def delete_at_position(self, position):
        if position<0 or position>=self.length():
            print("Invalid position")
            return
        if position==0:
            self.delete_at_beginning()
            return
        if position==self.length()-1:
            self.delete_at_ending()
            return
        current=self.head
        for _ in range(position):
            current=current.next
        previous_node=current.prev
        next_node=current.next
        previous_node.next=next_node
        next_node.prev=previous_node
        