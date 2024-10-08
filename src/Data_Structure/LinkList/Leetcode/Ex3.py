#Definition for singly-linked list.

from collections import deque

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        """
        You are given the head of a singly linked-list. The list can be represented as:

       L0 → L1 → … → Ln - 1 → Ln

        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
        Problem : 
        Input: head = [1,2,3,4,None]
        Output: [1,5,2,4,3]

        """

        node_queeu = deque()
        pass






if __name__ == "__main__":
    reverse= []
    list1 = deque([1,2,3,4,5,6])
    i = len(list1)
    for i in list1:
        #print(i)
        reverse.append(i)

        #i -= 1
    list1.peek()
    #list1.pop()
    list1.popleft()
    print(list1)




     


            



            
            



