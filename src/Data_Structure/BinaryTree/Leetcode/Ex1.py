# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        #Input: nums = [-10,-3,0,5,9]
        """-10 ,-3
        middel is 0 (left ) --> [left :2] 
        """
        


        def Reccucive(left, right):
            if left > right:
                return None 

            print(f"left {left}")
            print(f"rigth {right}")
            middel = (left+ right ) // 2 
            print(f" selected node index {middel}")
            print(f" node value {nums[middel]}")
            node = TreeNode(nums[middel])
            node.left =  Reccucive(left , middel -  1)
            node.right = Reccucive(middel + 1 , right)

            return node

        return Reccucive(0,len(nums)-1)
    
    def print_tree(self,out):
        tree = out
        while tree is not None:
            print(tree.val)
            if tree.left:
                tree
            else: 
                tree = tree.right

if __name__ =="__main__":
    nums = [-10,-3,0,5,9]

    algo = Solution()
    out = algo.sortedArrayToBST(nums=nums)
    #print(algo.print_tree(out))