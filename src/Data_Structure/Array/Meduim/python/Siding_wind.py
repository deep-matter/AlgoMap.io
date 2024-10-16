"""

You are given an array of integers nums, there is a sliding window of size 
k which is moving from the very left of the array to the very right. 
You can only see the k numbers in the window. 
Each time the sliding window moves right by one position.

Explainng the problem :
1. we will do have sub-Array of K means the length of sub-Array will be Equal to k-size 

2. the K-size should Equal the sub-Array 
Length means len(nums) + 1 <=  k || 

but do we nneed len(nums) included 0 to increament that by 1 

3. to split array based on K-size to take sub-Array we will use two Pointers one is Slow and other is fast 
which means now k --> number of items Sub-array takes 
edge-case : does K always greater than 0 if not is okay to return first item in the list to indiczted into with k - 1 
Return the max sliding window.:
                append.max(nums[i:j]) 
                len(num) + 1 <= k 
Example 1:
              i=0 --> i = 1    j = k + 1  --> j=
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3


Output: [3,3,5,5,6,7]




"""



class Solution_1(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """

        #edge-case : does K always greater than 0 
        #if not is okay to return first item in the list to indiczted into with k - 1 
        
        
        #split array based on K-size to take sub-Array we will use two Pointers one is Slow and other is fast 
        i = 0 
        j = k

        MaxItems = []
        length = 0

        # if k  <= 1 :
        #      MaxItems.append(nums[k-1])
        #      return MaxItems

        while j <= len(nums):
            SubArray = nums[i:j]
            if len(SubArray) < k:
                return nums[i]
            Max = max(SubArray)
            MaxItems.append(Max)

            i +=1 
            j +=1
            
        return MaxItems


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        from collections import deque
        queue = deque()

        output = []

        l = r = 0 

        while r < len(nums):
            while queue and nums[queue[-1]] < len(nums[r]):
                queue.pop()
            queue.append(r)

            if l > queue[0]:
                queue.popleft()

            if (r + 1) >=  k:
                output.append(nums[queue[0]])
                l +=1 
            
            r+=1 

        return output




        


if __name__ == "__main__":
    nums = [1,3,-1,-3,5,3,6,7]
    nums = [1]
    k = 1
    algo = Solution()
    out = algo.maxSlidingWindow(nums=nums,k=k)

    print(out)
    # i  , k = 0,3 

    
    # print(nums[i:k])
    # print(nums[i+1:k + 1])

    # print(len(nums))