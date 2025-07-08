class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums) - 1)

    # Binary search method
    def binarySearch(self, nums: List[int], target: int, left: int, right: int) -> int:
        if left > right:
            return left

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # If less, then search only left side
        elif target < nums[mid]:
            return self.binarySearch(nums, target, left, mid - 1)

        # If more, then search only right side
        else: 
            return self.binarySearch(nums, target, mid + 1, right)
