"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.


input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:

Input: head = [1], n = 1
Output: []

Example 3:

Input: head = [1,2], n = 1
Output: [1]

"""
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next is None:
            return head

        current = head

        while current:
            pervouis = current
            next_node = current.next
            current = current.next

            if next_node is None:
                pervouis = None
                current.next = next_node

                return head

class Solution(object):
    def removeNthFromEnd(self, head, n):
        fast = slow = head
        for i in range(n):
            fast= fast.next

        if not fast:
            return head.next
            
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next= slow.next.next
        return head





        











