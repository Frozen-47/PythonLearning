class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_rec(self.root, key)

    def _insert_rec(self, current, key):
        if key < current.key:
            if current.left is None:
                current.left = Node(key)
            else:
                self._insert_rec(current.left, key)
        elif key > current.key:
            if current.right is None:
                current.right = Node(key)
            else:
                self._insert_rec(current.right, key)

    def search(self, key):
        return self._search_rec(self.root, key)

    def _search_rec(self, current, key):
        if current is None or current.key == key:
            return current is not None
        if key < current.key:
            return self._search_rec(current.left, key)
        return self._search_rec(current.right, key)

if __name__ == "__main__":
    bst = BinarySearchTree()
    for val in [50, 30, 20, 40, 70, 60, 80]:
        bst.insert(val)
    print("Search 40 in BST:", bst.search(40))
    print("Search 90 in BST:", bst.search(90))
