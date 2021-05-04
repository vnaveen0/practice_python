# Property of BST:
# Every node on left is <=n, and every node on the right is >n.
class Node():
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def create_left(self, left_node):
        self.left = left_node
    def create_right(self, right_node):
        self.right = right_node

    def is_left(self):
        if self.left is None:
            return False
        else:
            return True

    def is_right(self):
        if self.right is None:
            return False
        else:
            return True

# BST
class Tree():
    def __init__(self, node):
        self.root = node
    # def insert(self, node):
    #     n = self.root
    #     while(1):
    #         if node.data <= n.data:
    #            print('do something')
    #         else:
    #             if n.left is None:
    #                 n.create_left(node)
    #                 break
    #             elif n.right is None:
    #                 n.create_right(node)
    #                 break
    #             else:
    #                 n = n.right

    def insert(self, node):
        n = self.root
        while(1):
            if node.data <= n.data:
                if n.left is None:
                    n.create_left(node)
                    break
                else:
                    n = n.left
            else:
                if n.right is None:
                    n.create_right(node)
                    break
                else:
                    n = n.right

    def preoder_traversal(self, n):
        if n is None:
            return
        self.preoder_traversal(n.left)
        self.visit(n)
        self.preoder_traversal(n.right)
        return

    def inoder_traversal(self, n):
        if n is None:
            return

        self.visit(n)
        self.inoder_traversal(n.left)
        self.inoder_traversal(n.right)
        return

    def postoder_traversal(self, n):
        if n is None:
            return
        self.postoder_traversal(n.left)
        self.postoder_traversal(n.right)
        self.visit(n)
        return

    def visit(self, n):
        print(n.data)


if __name__ == '__main__':
    # adjacency list
    arr = [12,14,60,34,50]
    root = Node(35)
    tree = Tree(root)
    for a in arr:
        node = Node(a)
        tree.insert(node)

    print('Pre Order')
    print('===============')
    tree.preoder_traversal(tree.root)
    print('In Order')
    print('===============')
    tree.inoder_traversal(tree.root)
    print('Post Order')
    print('===============')
    tree.postoder_traversal(tree.root)
    print()




