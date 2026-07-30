from collections import deque

class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)

if __name__ == "__main__":
    q = Queue()
    q.enqueue("Task 1")
    q.enqueue("Task 2")
    q.enqueue("Task 3")
    print("Front item:", q.peek())
    print("Dequeued item:", q.dequeue())
    print("Queue size:", q.size())
