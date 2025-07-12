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