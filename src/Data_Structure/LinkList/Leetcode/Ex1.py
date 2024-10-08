class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        
        while curr:
            next_node = curr.next  # Save the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev forward
            curr = next_node       # Move curr forward
        
        return prev  # prev will be the new head of the reversed list


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        """

    The number of nodes in the list is the range [0, 5000].
    -5000 <= Node.val <= 5000

        the Pronlem : Given the head of a singly linked list, reverse the list, and return the reversed list.
        Input: head = [1,2,3,4,5]
        Output: [5,4,3,2,1]

        Input: head = [1,2]
        Output: [2,1]

        head.value = 1 || head.next.value = 2
        tail.value = 2 || tail.next = None 

        swap the value over head and Tail --> head.value == head.next.value 
        swap the Value over tail and head --> tail.value == head.value  
        
        """
        per = None
        temp = head.next
        temp = head

        while head.next is not None:
            next_node = head.next
            head.next = per
            per = head.next










            

        