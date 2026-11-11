class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
class CircularLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            #CLL not empty
            new_node.next = new_node
            self.head = new_node
            return
        #CLL is not empty
        current = self.head
        while current.next != self.head:
            current = current.next
        new_node.next = self.head
        current.next = new_node
        self.head = new_node

    def insert_at_ending(self, data):
        new_node = Node(data)
         #CLL not empty
        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return
        #CLL is not empty
        current = self.head
        while current.next != self.head:
            current = current.next
            new_node.next=self.head
        current.next = new_node

    def insert_at_position(self, position, data):
        if position<0:
            print("Invalid position")
            return
        new_node = Node(data)
        if position==0:
            new_node.next=new_node
            self.head=new_node
            return
        current = self.head
        for _ in range(position-1):
            current=current.next
        new_node.next=current.next
        current.next=new_node

    def delete_at_beginning(self):
        #CLL is empty
        if self.head is None:
            print("CLL is empty")
            return
        #CLL has one element
        if self.head.next == self.head:
            self.head = None
            return
        #CLL has more than one element
        current = self.head
        while current.next != self.head:
            current = current.next
        self.head = self.head.next
        current.next = self.head

    def delete_at_ending(self):
        #CLL is empty
        if self.head is None:
            print("CLL is empty")
            return
        #CLL has one element
        if self.head.next == self.head:
            self.head = None
            return
        #CLL has more than one element
        current = self.head
        while current.next.next != self.head:
            current = current.next
        current.next = self.head
    def length(self):
        if self.head is None:
            return 0
        count=0
        current=self.head
        while True:
            count+=1
            current=current.next
            if current==self.head:
                break
        return count
    def display(self):
        current=self.head
        while True:
            print(current.data,end="->")
            current=current.next
            if current==self.head:
                break
        print("(back to head)")
cll=CircularLinkedList()
cll.insert_at_beginning(10)
cll.insert_at_beginning(20)
cll.insert_at_ending(30)
cll.insert_at_position(1,25)
cll.length()
cll.delete_at_beginning()
cll.delete_at_ending()
cll.display()
    