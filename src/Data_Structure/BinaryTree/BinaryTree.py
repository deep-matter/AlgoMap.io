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
    
    def contain(self,value):

        if self.root == None:
            return False 
        
        temp = self.root
        if temp.value == value:
            return True
        else:
            while(True):
                if temp is None:
                    return False

                if temp.value == value:
                    return True

                if value > temp.value:
                    
                    if temp.right is None:
                        if temp.value == value:
                            return True
                   
                    temp = temp.right

                    
                else:
                    if temp.left is not None:
                        if value == temp.value:
                            return True
                                       
                    temp = temp.left

    def recursion_contain(self,current_node,value):
        if current_node == None:
            return False 

        if current_node.value == value :
            return True
            
        if value < current_node.value:
            return self.recursion_contain(current_node.left ,value)

        if value > current_node.value:
            return self.recursion_contain(current_node.right,value)
        
        def __r_contain(self ,value):
            return self.recursion_contain(self.root,value)
    def Breath_firt_search(self):
        from collections import deque

        queue = deque()
        resultes = [ ]
        current_node = self.root

        queue.append(current_node)
        while len(queue) > 0:
            current_node = queue.popleft()
            resultes.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_nod.left)
            if current_node.right is not None :
                queue.append(current_node.right)
        return resultes




        
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
    tree.insert(5)
    print(tree.contain(3))
    print(tree.Breath_firt_search())






    tree.print_tree()
