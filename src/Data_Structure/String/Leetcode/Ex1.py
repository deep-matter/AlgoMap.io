"""

Given a string s, partition s such that every
substring
of the partition is a
palindrome
. Return all possible palindrome partitioning of s.


Example 1:

Input: s = "aab"
Output: [["a","a","b"],["aa","b"]]

Example 2:

Input: s = "a"
Output: [["a"]]
"""


case_1 = "aab"
case_2 =  "a"
slices = 0
chars = []
for char in case_1:
    chars.append(chars[char])
    slices +=1 
    

# for idx in chars:
    
    




print(chars)




# class Solution(object):
#     def partition(self, s):
#         """
#         :type s: str
#         :rtype: List[List[str]]
#         """

#         item = 0
#         char = []
#         for char in s:
#             char.append(s)
#             item += 1

#         while item < 0:
#             s = [char[item]]
#             item -= 1 

#         return s




        
            


