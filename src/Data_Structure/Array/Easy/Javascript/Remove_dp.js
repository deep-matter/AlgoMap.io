/**
 * @param {number[]} nums
 * @param {number} val
 * @return {number}
 */
var removeElement = function(nums, val) {
    var k = 0;
    for (var i = 0; i < nums.length ; i++){

        if ( nums[i] !== val){
            console.log(nums[i],val);
            nums[k] = nums[i];
            k++;

        }

       
    }
    return k ;
    
};


var nums = [3,2,2,3];
var val = 3;

output = removeElement(nums, val);
console.log(output)