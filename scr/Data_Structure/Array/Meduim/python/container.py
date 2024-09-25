class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        Algorithm : the Problem is to  compute the Squae between tow lines which are max in arraty 

        Height = [1,8,6,2,5,4,8,3,7] 

        each Point has (x , y ) ---> ( index , number):

        example : [0,1 ] , (1, 8 ), (2, 6) ,,,,, (8,7 )

        max  tow point in the array are (1, 8) and ( 8, 7 ) 

        keep in mind should start at point of following ( 1 -1 , 8 )---> (8 - 1, 7 )

        we need to take min value 

        now Squere_max  = (index -1 ) * 7 

        """

        # Solution 

        # intialzie left and right 

        left = 0
        right = len(height) -1 


        max_area = 0

        while left < right:

            distance = right - left 

            Square = min(height[left],height[right]) 

            curreht_area = distance * Square 

            max_area = max(max_area , curreht_area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

       

        return max_area









            


        # for val in height:
        #     left_arr.append(height[left])
        #     left -= 1



        # print(left_arr)

        # for val in height:
        #     right_arr.append(height[right])
        #     right += 1

        # print(right_arr)
        
        


if __name__ == "__main__":

    height = [1,8,6,2,5,4,8,3,7]

    Algo = Solution()
    output = Algo.maxArea(height)
    print(output)
