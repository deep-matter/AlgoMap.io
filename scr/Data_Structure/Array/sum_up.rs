use std::collections::HashMap;

fn two_sum(nums: Vec<i32>, target: i32) -> Option<(usize, usize)> {
    let mut map = HashMap::new();  // HashMap to store value and its index

    for (i, &val) in nums.iter().enumerate() {
        let complement = target - val;
        
        // Check if complement is in the map
        if let Some(&index) = map.get(&complement) {
            // If found, return the two indices as a tuple
            return Some((index, i));
        }
        
        // Insert the current value with its index into the map
        map.insert(val, i);
    }

    None  // If no such pair is found, return None
}

fn main() {
    let number_list = vec![3, 7, 2, 15];
    let target = 9;

    // Call two_sum and print result
    match two_sum(number_list, target) {
        Some((i, j)) => println!("Indices: {} and {}", i, j),
        None => println!("No two numbers sum up to the target"),
    }
}
