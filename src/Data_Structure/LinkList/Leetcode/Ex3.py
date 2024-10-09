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
        Input: head = [1,2,3,4,5]
        Output: [1,5,2,4,3]

        """
        dumy = ListNode(0)
        dumy.next = head
        current = dumy.next
        node_queeu = deque()

        while current:
            node_queeu.append(current)
            current = current.next

        even = False 
        current = current.next

        while node_queeu:
            node = node_queeu.pop() if even else node_queeu.popleft()
            node.next = None
            current = node
            even ^= True

        return head


        






if __name__ == "__main__":
    pass



     


            



            
            



