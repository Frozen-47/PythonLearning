import heapq

class MinHeap:
    def __init__(self):
        self._heap = []

    def push(self, item):
        heapq.heappush(self._heap, item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty heap")
        return heapq.heappop(self._heap)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty heap")
        return self._heap[0]

    def is_empty(self):
        return len(self._heap) == 0

    def size(self):
        return len(self._heap)

    def heapify(self, iterable):
        self._heap = list(iterable)
        heapq.heapify(self._heap)

if __name__ == "__main__":
    mh = MinHeap()
    items = [15, 3, 20, 1, 8, 12]
    print("Initial items:", items)
    mh.heapify(items)
    print("Smallest element (peek):", mh.peek())
    print("Popping elements in ascending order:")
    while not mh.is_empty():
        print(mh.pop(), end=" ")
    print()
