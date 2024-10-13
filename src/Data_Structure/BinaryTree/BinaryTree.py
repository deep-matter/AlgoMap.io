class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None




class BinaryTree(object):
    def __init__(self,value):
        node = Node(value=value)
        self.root = node

    def print_tree(self):
        tree = self.root
        while tree.left is not None and tree.right is not None:
            print(tree.value)



if __name__ =="__main__":
    tree = BinaryTree(1)
    tree.print_tree()
