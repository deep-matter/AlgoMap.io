### 1. Remove Duplicates from a Sorted Array

Given a sorted array, remove the duplicates **in place** such that each unique element appears only once. The relative order of the elements should be kept the same, and the function should return the number of unique elements. You should achieve this without using extra space for another array.

### 2. Two Sum

Given an array of integers and a target integer, find two numbers such that they add up to the target. The function should return the indices of the two numbers. Each input has exactly one solution, and you may not use the same element twice. The result should be provided in O(n) time.

## Solution Approaches

### 1. Remove Duplicates from a Sorted Array

This problem can be efficiently solved by using a **two-pointer approach**. The key idea is to traverse the array while keeping track of the position where the next unique element should be placed. By iterating through the array and comparing each element to the last unique one, we ensure that duplicates are skipped, and unique elements are shifted to the front.

- **Time Complexity**: O(n), where n is the number of elements in the array. We iterate through the array exactly once.
- **Space Complexity**: O(1), since the array is modified in place without using any additional data structures.

### 2. Two Sum

This problem is optimally solved by using a **hash map (dictionary)** to store previously seen elements and their indices. As we iterate through the array, for each element, we calculate the complement (i.e., `target - current element`). If the complement exists in the hash map, we know the current element and the complement add up to the target, and we can return their indices.

- **Time Complexity**: O(n), where n is the number of elements in the array. Each lookup and insertion in the hash map occurs in constant time.
- **Space Complexity**: O(n), due to the space required by the hash map to store elements and their indices.