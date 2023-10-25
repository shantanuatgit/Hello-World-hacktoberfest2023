class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def display(self):
        if not self.head:
            return
        temp = self.head
        while True:
            print(temp.data, end=' -> ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def get_length(self):
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
            count += 1
        return count

# Example usage:
clist = CircularLinkedList()
clist.append(1)
clist.append(2)
clist.append(3)
clist.append(4)

clist.display()  # Should print: 1 -> 2 -> 3 -> 4 ->

print("Length of Circular Linked List:", clist.get_length())  # Should print: 4
