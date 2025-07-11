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