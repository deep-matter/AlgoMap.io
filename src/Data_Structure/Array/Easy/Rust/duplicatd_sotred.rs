struct Solution;

impl Solution {
    pub fn remove_duplicates(nums: &mut Vec<i32>) -> i32 {
        // If the array is empty, return 0
        if nums.is_empty() {
            return 0;
        }

        // Pointer to track the position of the next unique element
        let mut k = 1;

        // Iterate through the array starting from the second element
        for i in 1..nums.len() {
            // If the current element is different from the last unique element
            if nums[i] != nums[k - 1] {
                // Move the unique element to the k-th position
                nums[k] = nums[i];
                k += 1;
            }
        }

        k as i32
    }
}

fn main() {
    let mut nums = vec![1, 1, 2, 2, 3, 4, 4, 5];
    let length = Solution::remove_duplicates(&mut nums);
    println!("New length: {}", length);
    println!("Modified array: {:?}", &nums[..length as usize]);
}
