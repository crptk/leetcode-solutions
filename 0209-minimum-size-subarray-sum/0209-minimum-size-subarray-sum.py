class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        length = len(nums)
        prefix = [0]
        for n in nums:
            prefix.append(prefix[-1] + n)
        subarray_size = float('inf')

        right_window = 0
        for i in range(length):
            for j in range(right_window, length):
                current_sum = prefix[j+1] - prefix[i]

                if current_sum >= target:
                    subarray_size = min(subarray_size, j - i + 1)
                    right_window = j
                    break

        return subarray_size if subarray_size != float('inf') else 0