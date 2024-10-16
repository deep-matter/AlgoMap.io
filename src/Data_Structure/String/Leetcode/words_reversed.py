class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        a = ""
        arr = []
        for i in range(len(s)):
            
            if s[i] == " " :
                arr.append(a)
                a = ""
                continue
            
            else :
                a += s[i]
        arr.append(a)
                
        arr = filter(None, arr)

        return " ".join(list(reversed(arr)))


if __name__ == "__main__":
    s = "the sky is blue"
    algo = Solution()
    out = algo.reverseWords(s)
    print(out)








            


        