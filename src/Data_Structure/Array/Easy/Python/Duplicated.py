class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        repeat = {}

        for idx , item in enumerate(nums):
            if not item in repeat.values():
                repeat[idx] = item
            else:
                return True
        return False 


if __name__ =="__main__":
    case_1 =  [1,2,3,1]
    case_2 = [1,2,3,4]
    case_3 = [0]
    case_4 = [3,3]
    Algo = Solution()
    output = Algo.containsDuplicate(case_2)
    print(output)
