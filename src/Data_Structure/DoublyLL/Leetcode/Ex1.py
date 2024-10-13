"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.


Add Two Numbers

You are given two non-empty linked lists, l1 and l2, where each represents a non-negative integer.

The digits are stored in reverse order, e.g. the number 123 is represented as 3 -> 2 -> 1 -> in the linked list.

Each of the nodes contains a single digit. You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Return the sum of the two numbers as a linked list.

Input: l1 = [1,2,3], l2 = [4,5,6]

Output: [5,7,9]

Explanation: 321 + 654 = 975.

Example 2:

Input: l1 = [9], l2 = [9]

Output: [8,1]

Constraints:

    1 <= l1.length, l2.length <= 100.
    0 <= Node.val <= 9
    
    
    """
class ListNode(object):
    def __init__(self,val=None):
        self.val = val 
        self.next = None 

    

class Solution(object):
    def SumTowNumbers(self, l1: ListNode , l2: ListNode)-> ListNode:
        dumy = ListNode()
        current = dumy
        carry= 0 

        while l1 != None and l2 != None and carry != 0:
            val_1 =  l1.val if l1 != None else 0
            val_2 =  l2.val if l2 != None else 0 

            SumUP = val_1 + val_2 + carry

            if SumUP % 10 == SumUP:
                carry = 0
            else:
                carry = SumUP // 10 
            
            SumUP = SumUP % 10 
            
            current.next = ListNode(val=SumUP)

            current = current.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dumy.next
            

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        while l1 or l2 or carry:
            l1_current = l1.val if l1 else 0
            l2_current = l2.val if l2 else 0

            total = l1_current + l2_current + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next


            if l1: l1 = l1.next
            if l2: l2 = l2.next

        return dummy_head.next




if __name__ == "__main__":
   


    c = 15 // 10
    #c = c % 10
    print(c)

