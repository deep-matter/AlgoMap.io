# LeetCode Code Challenges

This document contains solutions to several coding challenges from LeetCode, categorized by difficulty (Easy, Medium, Hard). Each solution includes a brief explanation of the problem, the approach used, and the complexity analysis.

## Easy Problems

- [Remove Duplicates from a Sorted Array](#1-remove-duplicates-from-a-sorted-array)
- [Two Sum](#2-two-sum)

## Medium Problems

- [Max Area of Container Problem](#3-max-area-of-container-problem)

---

### 1. Remove Duplicates from a Sorted Array

#### Problem Description
Given a sorted array, remove the duplicates **in place** such that each unique element appears only once. The relative order of the elements should be kept the same. The function should return the number of unique elements and modify the array in place without using extra space for another array.

#### Solution Approach
This problem can be solved using a **two-pointer approach**. As you traverse the array, you track the position where the next unique element should be placed. By iterating through the array and comparing each element with the last unique element, duplicates are skipped, and unique elements are shifted to the front.

#### Complexity

- **Time Complexity**: O(n), where n is the number of elements in the array. We iterate through the array exactly once.
- **Space Complexity**: O(1), as we modify the array in place without using extra space.

---

### 2. Two Sum

#### Problem Description
Given an array of integers and a target integer, find two numbers that add up to the target. Return the indices of the two numbers. Each input has exactly one solution, and you may not use the same element twice.

#### Solution Approach
This problem can be solved efficiently using a **hash map**. As you iterate through the array, for each element, you calculate the complement (`target - current element`). If the complement exists in the hash map, you return the indices of the complement and the current element.

#### Complexity

- **Time Complexity**: O(n), where n is the number of elements in the array. Each lookup and insertion in the hash map occurs in constant time.
- **Space Complexity**: O(n), due to the space required by the hash map to store elements and their indices.

---

### 3. Max Area of Container Problem

#### Problem Description
Given an integer array representing the height of vertical lines, find two lines that form a container with the x-axis such that the container holds the most water.

#### Solution Approach
This problem can be solved using the **two-pointer technique**:
1. Initialize two pointers: one at the start (`left`) and one at the end (`right`) of the array.
2. Calculate the area between the lines represented by these two pointers. The area is determined by the shorter of the two heights (`min(height[left], height[right])`) multiplied by the distance between the two pointers (`right - left`).
3. Track the maximum area encountered.
4. Move the pointer pointing to the shorter height inward, as this is the only way to potentially increase the area.
5. Continue until the two pointers meet.

#### Complexity

- **Time Complexity**: O(n), where n is the number of elements in the array. We traverse the array once using two pointers.
- **Space Complexity**: O(1), as only a few extra variables are used to store the pointers and area.
