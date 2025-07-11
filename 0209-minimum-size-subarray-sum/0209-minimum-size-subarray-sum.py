class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        subarray_size = float("inf")

        for r in range(len(nums)):
            total += nums[r]

            while total >= target:
                subarray_size = min(subarray_size, r - l + 1)
                total -= nums[l]
                l += 1


        return subarray_size if subarray_size != float('inf') else 0

'''
Written by Edrees

This solution implements the sliding window technique, where you keep a left and right pointer, and shift both pointers forward until the desired result is achieved. 

In this case we needed to get the smallest sized window that when summed, equals the target. This can be done in the sliding window by having a while loop within the window once it realizes that the requirement (total ≥ target) is met, once it is, we will decrement the window from the left (shift it forward by 1) each time until it becomes small enough that the requirement isn’t met anymore. This ensures that all values are covered, and this also gets only minimum size of the window using the min() function, so we don’t lose track of the smallest sized window we’ve found during the algorithms run time. 

The reason we set subarray_size to inf in the beginning is because any value that is above the length of the array is invalid or can never be reached, so we just chose an arbitrarily large number to set it to. All that matters is that it’s unable to be reached by the algorithm so we don’t accidentally return something other than 0 if we don’t find the target window.
'''