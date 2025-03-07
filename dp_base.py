import random

def max_subarray_divide_and_conquer(arr, left, right):
    # Base case: only one element
    if left == right:
        return arr[left]

    mid = (left + right) // 2

    # Recursive case: calculate for left, right, and crossing sum
    left_max = max_subarray_divide_and_conquer(arr, left, mid)
    right_max = max_subarray_divide_and_conquer(arr, mid + 1, right)
    cross_max = max_crossing_sum(arr, left, mid, right)

    # The maximum subarray is the max of the left, right, and crossing
    return max(left_max, right_max, cross_max)

# Loop through array sizes from start_n to end_n, incrementing by increment_n
for n in range(start_n, end_n + increment_n, increment_n):
    arr = [random.randint(-100, 100) for _ in range(n)]

    max_subarray_dynamic_programming(arr)
