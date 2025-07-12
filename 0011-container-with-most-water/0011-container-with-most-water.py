class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        highest_area = 0

        while l != r:
            hl, hr = height[l], height[r]
            distance = r - l # works
            area = min(height[r], height[l]) * distance
            highest_area = max(highest_area, area)

            if height[l] < height[r]:
                l += 1
                while l < r and height[l] <= hl:
                    l += 1
            else:
                r -= 1
                while r > l and height[r] <= hr:
                    r -= 1

        return highest_area


'''
My previous solution:
class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        highest_area = 0

        while l != r:
            distance = r - l # works
            area = min(height[r], height[l]) * distance
            highest_area = max(highest_area, area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return highest_area

In this solution we are asked to find the container with the biggest area, which is essentially finding the two heights that when calculated with the distance, will formulate the largest area. To do this, we set up one left pointer in the beginning, and one right pointer at the end of the array. Then we calculate the area between them being the distance between them multiplied by the shorter height, we check if its over the current maximum area, we check which pointer is smaller:

- If the left pointer is smaller, shift it over to the right once
- If the right pointer is smaller, shift it over to the left once.

This algorithm keeps looping until the left and right pointers meet.

In the better solution that was submitted, the key difference is in the last step when the pointers are shifted - it keeps shifting until it finds a height that is taller than the height the current pointer is pointing to. This optimizes the algorithm so that it doesn’t need to make redundant calculations by only calculating the larger heights.
'''