class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        
        left = 0
        right = len(height) - 1
        left_max = 0
        right_max = 0
        water = 0
        
        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left] # Set a new wall/max
                else:
                    water += left_max - height[left] # Fill up the current block so far from the wall/max
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water


'''
Solution by Crptk

This solution basically sets two points left and right, and keeps iterating until they cross over each other.

For both the left and right sides, we instead of filling up the water only after we reach another wall, we're actually
filling the water as we go by subtracting the current index on each side to the maximum value/wall on each side, which gives
us the water to store at that current index. Then when we find a wall that's larger, we know that we can't store water there
but we can instead set it to the new maximum wall. This continues until the left and right pointers cross.

Time complexity: O(n)
Space complexity: O(1)
'''