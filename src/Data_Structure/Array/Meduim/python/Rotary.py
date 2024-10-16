"""
    Given an integer array nums, rotate the array to the right by k steps, where k is non-negative
    Input: nums = [1,2,3,4,5,6,7], k = 3
    Output: [5,6,7,1,2,3,4]
    nput: nums = [-1,-100,3,99], k = 2
    Output: [3,99,-1,-100]
"""

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        k = k % l
        nums2 = list(nums)
        nums[k:l] = nums2[0:l-k]
        nums[0:k] = nums2[l-k:l]
        return nums

                    




   
        
if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7]
    arr1 = [-1,-100,3,99]
    # m = len(arr) // 2
    # print(arr[m])
    #print(len(arr1) % 2)
    algo = Solution()
    out = algo.rotate(arr , 3)
    print(out)



            



