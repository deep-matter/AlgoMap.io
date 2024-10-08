"""

the problem Statment :  merge to Sorted LinkListed 

"""
class ListNode(object):
    """
    the class contain the Node list1 and list2


    """
    def __init__(self,val= 0 , next = None ):
        self.val = val 
        self.next = next


class Solution(object):
    def mergeTwoLists(self,list1 , list2):
        """
        list1 : dtype ListNode
        list2 : dtype ListNode 
        """
        """
        Solution Algorithm :

        list1 : [1,2,3]
        list2 : [1,3,4]

        output [1,1,2,3,4]

        """ 

        new_list = list1


        while list1:
            if list1.val == list2.val:
                new_list = list1
                new_list.next = list2.next

            if list1.val < list2.val:
                new_list.next = list1

            if list1.val > list2.val:
                new_list.next = list2
               

            list1 = list1.next
            list2 = list2.next

        return new_list



class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2 
        if list2 is None:
            return list1 
        
        if list2.val < list1.val:
            list1, list2 = list2, list1

        head = list1 

        while list1 and list1.next and list2:
            if list2.val < list1.next.val:
                tmp = list2
                list2 = list2.next 
                tmp.next = list1.next 
                list1.next = tmp 
                list1 = list1.next 
            else:
                list1 = list1.next 

        if list1.next is None:
            list1.next = list2

        return head 




                






























