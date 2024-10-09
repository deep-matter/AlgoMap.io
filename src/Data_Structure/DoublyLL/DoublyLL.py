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
    DLL.repend(8)



    DLL.print_dll()

