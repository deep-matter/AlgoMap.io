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
        
        self.tail.next = new_nodels 
        new_node.pres = self.tail
        self.tail = new_node
        self.length +=1
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


    DLL.print_dll()

