# Maximum Contiguous Subarray Sum

## Problem Description
Given an array of integers, the task is to **find the contiguous subarray (containing at least one number) that has the largest sum** and return its sum along with its **starting and ending indices**.

For example, given the array `[-2,1,-3,4,-1,2,1,-5,4]`,  
the contiguous subarray with the largest sum is `[4,-1,2,1]`, with a **maximum sum of 6**.

---

## Input Format
- An array `arr` containing `N` integers is provided. (`1 ≤ N ≤ 10,000`)
- Each element satisfies `-100 ≤ arr[i] ≤ 100`.

---

## Output Format
- The output consists of **three integers**:
  - `start_index`: The **0-based index** where the maximum sum subarray starts.
  - `end_index`: The **0-based index** where the maximum sum subarray ends.
  - `max_sum`: The maximum sum of the contiguous subarray.

---

## Example Input & Output

### Example 1
#### Input:
```
1 -2 3 10 -4 7 2 -5
```
#### Output:
```
2 6 18
```
**Explanation:**  
The subarray `[3, 10, -4, 7, 2]` (from index **2 to 6**) has the maximum sum **18**.

---

### Example 2
#### Input:
```
-2 1 -3 4 -1 2 1 -5 4
```
#### Output:
```
3 6 6
```
**Explanation:**  
The subarray `[4, -1, 2, 1]` (from index **3 to 6**) has the maximum sum **6**.

