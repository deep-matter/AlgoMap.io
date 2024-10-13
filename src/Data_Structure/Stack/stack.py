class Node(object):
    def __init__(self,value):
        self.value = value
        self.next = None



class Stack(object):
    def __init__(self,value):
        node = Node(value)
        self.top = node
        self.height = 1

    def push(self, value):
        new_node = Node(value=value)

        if self.height == 0 :
            self.top = new_node
            return self.top

        current = self.top
        self.top = new_node
        self.top.next = current

        self.height += 1
        return True
    def pop(self):

        if self.top.next is None or self.height == 0:
            return False

        current = self.top 
        self.top = self.top.next
        current.next = None
        
        self.height -=1 

        return current

        
        




    def  print_stack(self):
        temp = self.top 

        while temp is not None:
            print(temp.value)
            temp = temp.next



if __name__ =="__main__":
    stack = Stack(value=1)
    # push method 
    stack.push(3)
    # pop method 
    stack.pop()
    stack.print_stack()