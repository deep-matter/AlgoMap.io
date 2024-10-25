"""

You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order,
 starting with word1. If a string is longer than the other, 
 append the additional letters onto the end of the merged string.
"""



class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        s = ""
        rest = 0
        if len(word1) == len(word2):
        for (item_i , item_2) in zip(word1, word2):
            
                s+= item_i + item_2 
            else:
                s+= item_i + item_2 
                rest += 1

        return s 


if __name__ =="__main__":
    # word1 = "abc"
    # word2 = "pqr"
    word1 = "ab"
    word2 = "pqrs"
    algo = Solution()
    out = algo.mergeAlternately(word1, word2)
    print(out)
