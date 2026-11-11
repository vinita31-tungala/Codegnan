# Linkedlist
# --> Linear Data Structure,
# --> data can be represented in nodes,
# --> node contains data and address of next element.
# Why do we need linkedlist:
# --> We can store unlimited data,
# --> data can be add randomly,
# --> no fixed size

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Insert at ending
    def insert_at_ending(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    # Insert at specific position
    def insert_at_position(self, position, data):
        if position < 0:
            print("Invalid position")
            return

        if position == 0:
            self.insert_at_beginning(data)
            return

        current = self.head

        for _ in range(position - 1):
            if current is None:
                print("Invalid position")
                return
            current = current.next

        if current is None:
            print("Invalid position")
            return

        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node

    # Delete at beginning
    def delete_at_beginning(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        self.head = self.head.next

    # Delete at ending
    def delete_at_ending(self):
        if self.head is None:
            print("Linkedlist is empty")
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head

        while current.next.next is not None:
            current = current.next

        current.next = None

    # Delete at specific position
    def delete_at_position(self, position):
        if position < 0:
            print("Invalid position")
            return

        if self.head is None:
            print("Linkedlist is empty")
            return

        if position == 0:
            self.head = self.head.next
            return

        current = self.head

        for _ in range(position - 1):
            if current.next is None:
                print("Invalid position")
                return
            current = current.next

        if current.next is None:
            print("Invalid position")
            return

        current.next = current.next.next

    # Search an element
    def search(self, value):
        current = self.head

        while current is not None:
            if current.data == value:
                return True

            current = current.next

        return False

    # Find length
    def length(self):
        count = 0
        current = self.head

        while current is not None:
            count += 1
            current = current.next

        return count

    # Reverse linked list
    def reverse(self):
        previous = None
        current = self.head

        while current is not None:
            next_node = current.next
            current.next = previous
            previous = current
            current = next_node

        self.head = previous

    # Detect cycle
    def has_cycle(self):
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True

        return False

    # Display linked list
    def display(self):
        current = self.head

        while current is not None:
            print(current.data, end=" -> ")
            current = current.next

        print("None")


# Main program
ll = Linkedlist()

ll.insert_at_beginning(10)
ll.insert_at_beginning(5)
ll.insert_at_ending(20)
ll.insert_at_position(2, 15)

ll.display()

print("Length:", ll.length())
print("Search 15:", ll.search(15))
print("Cycle detected:", ll.has_cycle())

ll.delete_at_beginning()
ll.display()

ll.delete_at_ending()
ll.display()

ll.delete_at_position(1)
ll.display()

ll.reverse()
print("Reversed linked list:")
ll.display()
ll.search(20)
print("Search 20:", ll.search(20))
print("Length:", ll.length())
print("Reversed linked list:")
ll.reverse()
ll.display()
print(ll.has_cycle())
