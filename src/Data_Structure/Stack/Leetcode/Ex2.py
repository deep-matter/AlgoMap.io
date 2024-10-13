class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left_part = 0
        right_part = len(s) - 1
        while left_part < len(s):
            if s[left_part] == s[right_part]:
                print(s[left_part], s[right_part])
            elif s[left_part + 1] == s[left_part]:
                print(s[left_part], s[right_part])
            else:
                return False
            left_part += 1
            right_part -= 1
        return True

if __name__ == "__main__":
    part = "()"
    algo = Solution()
    out = algo.isValid(part)
    print(out)