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

'''
In this solution using binary search, I checked specifically for if the value at the middle is over the value on the right pointer, if it is, that means that the minimum has to lie in that area, since the pivot would be there. If not, then the minimum is either the current middle or the leftmost side of the array. This covers all edge cases and is the most simple O(logn) solution I could think of. 

Example:

1. [4,5,6,7,0,1,2] | mid = 7 | Starting array
2. [0,1,2] | mid = 1 | Cut off right left side since minimum is located on right side
3. [0, 1] | mid = 0 | Cut off right side since minimum is located on left  side
4. [0] | mid = 0 | Only one element left, which means m == r, which means it returns nums[m]
'''