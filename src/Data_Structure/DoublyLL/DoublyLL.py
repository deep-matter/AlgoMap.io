class Node:
    def __init__(self , value):
        self.value = value
        self.next= None
        self.pres = None


class DoublyLinklist:
    def __init__(self, value):
        node = Node(value=value)
        self.head = node
        self.tail = node
        self.length = 1

    def append(self, value):
        new_node = Node(value=value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        
        self.tail.next = new_node 
        new_node.pres = self.tail
        self.tail = new_node
        self.length +=1
        return True

    def pop(self):

        if self.length == 0 :
            return False

        if self.length == 1:
            self.tail = None 
            self.head = None 
        else:
            temp = self.tail
            self.tail = self.tail.pres 
            self.tail.next = None 
            temp.pres = None
            self.length -= 1
        return True

    def repend(self,value):
        new_node = Node(value=value)

        if self.head is None :
            self.head = new_node
            self.tail = new_node
        
        else:
            temp = self.head
            new_node.next = temp
            self.head = new_node
            self.length += 1

        return True

    def pop_first(self):

        if self.length == 0:
            return False 
        
        if self.length == 1:
            self.head = None 
            self.tail = None
        else:
            next_head = self.head.next
            self.head.pres = None
            self.head = next_head

            self.length -=1 
        
        return True

    def get_index_node(self,index):
        if index < 0 or index > self.length:
            return False 
        forward = self.head
        if index < (self.length // 2 ):
            for _ in range(index):
                forward = forward.next
        else:
            forward = self.tail
            for _ in range(self.length - 1 , index , -1):
                forward = forward.pres

        return forward

            



        
        




        






    def print_dll(self):
        temp = self.head 
        while temp is not None:
            print(temp.value)
            temp = temp.next




if __name__ == "__main__":
    DLL = DoublyLinklist(7)
    ## Append Method in DLL 
    DLL.append(5)
    DLL.append(4)
    DLL.append(4)
    #DLL.pop()
    DLL.repend(4)
    #DLL.repend(8)
    DLL.pop_first()
    DLL.get_index_node(0)
    print(DLL.get_index_node(0).value)
    print(DLL.get_index_node(2).value)


    DLL.print_dll()

