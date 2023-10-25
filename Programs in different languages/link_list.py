class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
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

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=' -> ')
            temp = temp.next
        print("None")

# Example usage:
slist = SinglyLinkedList()
slist.append(1)
slist.append(2)
slist.append(3)
slist.append(4)

slist.display()  # Should print: 1 -> 2 -> 3 -> 4 -> None
