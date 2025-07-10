class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        target_indexes = [-1, -1]
        for i in range(len(nums)):
            if nums[i] == target:
                target_indexes[0] = i
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == target:
                target_indexes[1] = i
                break
        return target_indexes