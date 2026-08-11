class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    res = []
    if root:
        res.extend(inorder_traversal(root.left))
        res.append(root.val)
        res.extend(inorder_traversal(root.right))
    return res

def preorder_traversal(root):
    res = []
    if root:
        res.append(root.val)
        res.extend(preorder_traversal(root.left))
        res.extend(preorder_traversal(root.right))
    return res

def postorder_traversal(root):
    res = []
    if root:
        res.extend(postorder_traversal(root.left))
        res.extend(postorder_traversal(root.right))
        res.append(root.val)
    return res

if __name__ == "__main__":
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    print("Inorder:", inorder_traversal(root))
    print("Preorder:", preorder_traversal(root))
    print("Postorder:", postorder_traversal(root))
