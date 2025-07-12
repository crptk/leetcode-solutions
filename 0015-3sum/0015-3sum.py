class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:            
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res


'''
Solution by Edrees Amiri

In this solution we are asked to find every set of three numbers in the array `nums` such that the sum of each set equals zero. To do this, we start by sorting the list since it’ll make it a lot easier to find duplicates. Then we iterate through the whole list using a for loop with a pointer `i` . 

Inside the loop, we check if it’s a duplicate by checking the number before it, if it isn’t, then we grab a left pointer being the number after i, and a right pointer being the last value in the array. Afterwards, we check if the sum of all three numbers is zero, if it’s over zero, then we know that we should shift the right pointer down since it’s too high, if it’s less than zero, then we know that we should shift the left number upwards since it’s too low. Otherwise if it equals zero, then we found a valid set so we append it to our result list of sets.

Now we need to shift our pointers forward. In order to do so with the least code, we shift our left pointer forwards until it’s unique and less than the right pointer.
'''