class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []

"""
This solution uses left and right pointers to traverse the array.

We take advantage of the fact that the array is in increasing order to update the left and right pointers
such that if their sum is above the target, we increment the left pointer. If it's below, we decrement
the right pointer. This ensures that with each increment/decrement, we get closer to the target and never
skip any possible combination whos sums = target.

Time complexity: O(n)
Space complexity: O(1)
""" 