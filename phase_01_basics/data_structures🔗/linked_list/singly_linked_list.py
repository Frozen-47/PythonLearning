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
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def delete_value(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return True
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if not current:
            return False
        prev.next = current.next
        return True

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" -> ".join(elements) if elements else "Empty List")

if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.append(10)
    sll.append(20)
    sll.append(30)
    sll.prepend(5)
    print("Singly Linked List:")
    sll.display()
    print("Search 20:", sll.search(20))
    sll.delete_value(20)
    print("After deleting 20:")
    sll.display()
