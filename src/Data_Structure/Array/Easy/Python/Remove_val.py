class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        for i in range(len(nums)):
            if val in nums:
                nums.remove(val)
        return len(nums)


# class Solution(object):
#     def removeElement(self, nums, val):
#         nums[:] = [i for i in nums if i !=val]
#         print(nums[:])
#         return len(nums)
    

if __name__ =="__main__":
    nums = [3,2,2,3]
    val = 3
    Algo = Solution()
    output = Algo.removeElement(nums, val)
    print(output)

