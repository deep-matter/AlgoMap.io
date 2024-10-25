#Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        output = []

        if not root:
            return root

        if root:
            current_node = root

        def TreeTraveresal(self,current_node):
            # edeg case if Root is Null 
            if current_node:
                output.append(current_node,val)

                if current_node.left is not None:
                    TreeTraveresal(current_node.left)
                
                if current_node.right is not None:
                    TreeTraveresal(current_node.right)

        TreeTraveresal(current_node)

    return output


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        from collections import deque

        output = []
        queue = deque()

        if not root :
            return root 

        queue.append(root)

        while len(queue) > 0:
            Level = []
            lengthQue = len(queue)
            for i in range(lengthQue):
                current_node = queue.popleft()
                if current_node:
                    Level.append(current_node.val)
                    queue.append(current_node.left)
                    queue.append(current_node.right)
            if Level:
                output.append(Level)
    return output
            



        
        

        



            








        