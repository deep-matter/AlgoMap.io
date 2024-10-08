class Node:
    def __init__(self, value):
        self.value = value
        self.next = None ### {"value": value , "next": node }

class LinkedList:
    def __init__(self,value):
        node = Node(value)
        self.head = node #{value : value , Next : node}
        self.tail = node #{value : value , Next : None}
        self.length = 1

    def append(self, value):
        new_node = Node(value=value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node

        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length +=1 

        return True
       
    def perappend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        
        self.length += 1 

        return True

    def pop_first(self):
        if self.length == 0:
            return None
        else:
            temp = self.head
            self.head = self.head.next
            self.length -= 1

        if self.length == 0:
             self.tail = None

        return True
        
    def pop(self):
        if self.head is None:
            return "list is empty"
        
        temp = self.head   
        per = self.head

        while temp.next is not None:
            per = temp
            temp = temp.next

        self.tail = per
        self.tail.next = None

        self.length -= 1 

        if self.length == 0:
            self.head = None
            self.tail = None 

        return temp
    
    def get(self, index):

        if self.length < index and index < 0 :
            return None

        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp 
    
    def set_value(self, index , value):
        if self.length < index and index < 0 :
            return None

        temp = self.head

        for _ in range(index):
            temp = temp.next

        temp.value = value
        return temp

    
            
    def insert(self, index , value):
        new_node = Node(value=value)

        if index < 0 or index > self.length:
            return False

        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1

    def remove(self,index):
        if index < 0 or index > self.length:
            return False
        if index == 0 :
            return self.pop_first()
        if index ==  (self.length - 1):
            return self.pop()

        previous = self.get(index - 1)
        temp = previous.next
        previous.next = temp.next 
        temp = None
        self.length -= 1
        return True

    def reverse(self):
        """
                                              Head                     Tail 
                                               ^                        ^     
                                               |                        |
        orign_list =  [4 ,1 , 2 , 3, None ] ## 4 --> 1 --> 2 --> 3 --> None

        reversed_list = [ None , 3, 2, 1, 4 ] ## None --> --> 3 --> 2 --> 1 --> 4 

        """
        reversed_list = None # None --> 
        head = self.head # iter 0 : 1 ||

        while head is not None:
            next_node = head.next # iter 0 : 1 || iter 1 : 2 iter 2 : 3 || iter 4 : None
            head.next = reversed_list # iter 0 : None || iter 1 : 2 || iter 2 : 3 || iter 4 : None 
            reversed_list = head   # iter 0 : None || iter 1 : 2 || iter 2 : 3 || iter 4 : None |
            head = next_node
        
        self.head = reversed_list
        return self.head # iter 0 : 1 ||

    def middil_node(self):

        averge_node = self.length // 2 
    
        if isinstance(averge_node, float):
            averge_node = int(averge_node) + 1


        temp = self.head
        for middl in range(self.length):
            temp = temp.next
            if middl == averge_node:
                 self.head = temp
                 return self.head
        #temp = middil_node_list
        return temp

    def print_list(self):
        temp = self.head
        # for _ in range(3):
        #     temp = temp.next
        #     print(temp.value)

        while temp is not None:
            print(temp.value)
            temp = temp.next
            
if __name__ == "__main__":
    linklist = LinkedList(2)
    linklist.perappend(1)
    linklist.perappend(4)

    linklist.append(3)



    # #print(linklist.print_list())
    # node = linklist.get(0)
    # value = linklist.set_value(1, 3)
    # print(f"node get index at 0: {node.value}")
    linklist.insert(2,6)
    #linklist.remove(2)
    print(linklist.print_list())
    linklist.middil_node()
    print(linklist.print_list())

   

        
        
       
       







