from collections import deque

class Solution(object):
    def buildArray(self, target, n):
        """
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        
        counter = 1
        length = len(target) - 1 
        target_ops = []

        for i in target:
            while counter < i:
                target_ops.append("Push")
                print(counter, i)
                target_ops.append("Pop")
                print(counter, i)
                counter +=1 
                print(counter, i)
            target_ops.append("Push")
            counter +=1 
            print(counter, i)
        return target_ops


if __name__ =="__main__":
    target =[1,2,3]
    n = 3
    algo = Solution()
    out = algo.buildArray(target=target,n=n)
    print(out)
   



