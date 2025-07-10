class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return nums[0] if nums[0] < nums[1] else nums[1]
        min = self.binarySearch(nums)

        return min

    def binarySearch(self, nums):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            # 3 elements left 
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                return nums[m]
        