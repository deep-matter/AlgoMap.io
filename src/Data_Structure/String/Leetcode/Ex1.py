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


def recur(s,p):
    if not s:
        res.append(p)
    for i in range(len(s)):
        if s[:i+1] == s[:i+1][::-1]:
            recur(s[i+1:],p+[s[:i+1]])
    res = []
    recur(s,[])
    return res




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




        
            


