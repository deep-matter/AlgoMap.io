class Solution(object):
    def removeDuplicates(self, nums):
        """
        Removes duplicates from a sorted array in-place and returns the number of unique elements.
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        
        k = 1
        
        for i in range(1, len(nums)):
            print(i, k - 1)
            if nums[i] != nums[k - 1]:
                # print(nums[i])
                # print(nums[k - 1])
                print(k , i )
                nums[k] = nums[i]  
                # print(nums[k] , nums[i]   )
                k += 1
        
        return k 




if __name__ =="__main__":
    algo = Solution()
    num = [0,0,1,1,1,2,2,3,3,4]
    k    = algo.removeDuplicates(num)
    print(k  )
   
       
    