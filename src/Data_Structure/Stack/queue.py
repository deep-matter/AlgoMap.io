class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue(object):
    def __init__(self,value):
        node = Node(value=value)
        self.first = node
        self.last = node 
        self.length = 1 

    def Enqueue(self,value):
        new_node = Node(value= value)

        if self.length == 0 :
            self.first = new_node
            self.last = new_node

        else:

            current = self.last
            current.next = new_node
            self.last = current 
            self.length +=1

        return True

    def Dequeue(self):

        if self.first is None :
            return False 
        
        current = self.first
        self.first=  current.next
        current.next = None 
        self.length -=1 

        return True





    
    def print_queue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp= temp.next


if __name__ =="__main__":
    queue = Queue(3)
    # Euqueu 
    queue.Enqueue(2)
    # Dequeue
    queue.Dequeue()
    queue.print_queue()