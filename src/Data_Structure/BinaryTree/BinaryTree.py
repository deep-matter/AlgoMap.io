class Node(object):
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None




class BinaryTree(object):
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value=value)

        if self.root == None:
            self.root = new_node
            return True

        else:
            temp = self.root
            while (True):
                if temp.value == new_node.value:
                    return False 
                if temp.value > new_node.value:
                    if temp.left is None:
                        temp.left = new_node
                        return True
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = new_node
                        return True

                    temp = temp.right
        


        

        
        

    def print_tree(self):
        if self.root == None :
            print(self.root)
        tree = self.root
        while tree is not None:
            print(tree.value)
            if tree.left:
                tree
            else:
                tree = tree.right



if __name__ =="__main__":
    tree = BinaryTree()
    tree.insert(1)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(2)





    tree.print_tree()
