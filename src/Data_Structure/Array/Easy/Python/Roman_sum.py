




"""
pesuecode:

1. we have sympol with value I --> 1 , X --10

we need to store the symbol in hashSet : key --> value : Symbol --> Value 
"""
"""
hash_set["I"] = 1 
# version JS 

let HashSet = new Map("I":1, "V":5 ,,,,,,,)


Logic : 

case 1 : IIX = 12 --> I =1 , 1 = 1 , X = 10 
Roman = "IIX" : items "I ,I , X " -- : Position --> I : 0 , I:1 , X : 2

Res = 0

Loop idx in IIX: then --> iter 0  --> Idx --> I  : idx = I  
    log(idx)

    I = 1 : hash_set[idx]
    I = 1 : hash_set[idx]
    X = 10 : hash_set[idx]

    Res += hash_set[idx] ---> Res = Res + 0  

    return Res
"""

# Data Struct HashMAp : Key --> Value : I --> 1 

# version Python
hash_set = {

"I": 1, 
"V":5,
"X":10,
"L":50,
"C":100,
"D":500,
"M":1000
}

# print(hash_set["I"])
# print(hash_set["I"])
# print(hash_set["X"])
# print(hash_set.keys())
# print(hash_set.values())

#Res = hash_set["I"] + hash_set["I"] + hash_set["X"]

# print(Res)


# for key , value in hash_set.items():
#     print(f"Symbols  : {key} :  value : {value}")


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        # intialize the Res at 0 to be update 

        RES = 0 
        Roman = ["CM" ,"XC" , "IV"]
        i = 0 
        j = 1
        #s = "LVIII"
        hash_set = {

            "I": 1, 
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
            }
        i = 1
        for _ in s :
            #Roman = ["CM" ,"XC" , "IV"]
            if i > len(s):
                return RES
            else:
                rom = s[i] + s[i - 1]
                print(rom)

                if rom in Roman:
                    RES += ( - hash_set.get(s[i])  +  hash_set.get(s[i - 1]))
                    print(RES)
                else: 
                    RES += hash_set.get(s[i - 1])
            
            
                i += 1
        return RES


class Solution(object):
    def romanToInt(self, s):
        numerals = {
            "I": 1,
            "V": 5,
            "X": 10, 
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        
        # i = len(s)-1
        # num = 0

        # while i >= 0:
        #     if i != 0 and numerals[s[i]]>numerals[s[i-1]]:
        #         print('sub' + str(numerals[s[i]] - numerals[s[i-1]]))
        #         num += numerals[s[i]] - numerals[s[i-1]]
        #         i-=2
        #     else:
        #         print('add' + str(numerals[s[i]]))
        #         num += numerals[s[i]]
        #         i-=1
        # return num
        i = len(s)-1
        num = 0
        while i >= 0:
            if i != 0 and numerals[s[i]] > numerals[s[i-1]]:
                num += numerals[s[i]] - numerals[s[i-1]]
                i -= 2
            else:
                num += numerals[s[i]]
                i -= 1
                
        return num




if __name__ == "__main__":
    s = "MCMXCIV"
    algo = Solution()
    output = algo.romanToInt(s)
    print(output)
    #print(s[0])

        







