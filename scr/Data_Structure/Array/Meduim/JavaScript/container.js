/**
 * @param {number[]} height
 * @return {number}
 */


var maxArea = function(height) {
    // intialize the tow itretation left and Right 

    let left = 0
    let right = height.length - 1 ;
    let Area = 0 ;

    while (left < right){

        var Distance = right - left ;
        var newArea = Math.min(height[left],height[right]) * Distance

        Area = Math.max(Area , newArea) ;

        if (height[left] < height[right]){
            left++ ;
        }else{
            right-- ;

        }    
   }

   return Area
  
};


var height = [1,8,6,2,5,4,8,3,7]
const newArea = maxArea(height)
console.log(newArea)