class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def display_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print("None")

    def display_backward(self):
        temp = self.head
        while temp and temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.prev
        print("None")

# Example usage:
dlist = DoublyLinkedList()
dlist.append(1)
dlist.append(2)
dlist.append(3)
dlist.append(4)

print("Forward:")
dlist.display_forward()  # Should print: 1 <-> 2 <-> 3 <-> 4 <-> None

print("Backward:")
dlist.display_backward()  # Should print: 4 <-> 3 <-> 2 <-> 1 <-> None
