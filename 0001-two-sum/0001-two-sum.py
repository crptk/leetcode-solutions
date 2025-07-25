class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, n in enumerate(nums):
            c = target - n
            if c not in nums_dict:
                nums_dict[n] = i
            else:
                return [i, nums_dict[c]]

'''
Solved by Edrees

In order to solve this problem my first instinct was to use two pointers, one to keep track of each element in the array (traverse through the whole array from left to right), and another to traverse from the first pointer to the end to check if the two values sum to the target. I knew this wasn’t an efficient solution, but I had to start somewhere. 

The better solution is to use dictionaries to iterate through the array from left to right, and store each value with its index in a hashmap, and with each value iterated, we check if the target minus that value is present in the hashmap. If it is, return the index of both values. This is a much lower time complexity than O(n^2) since at worst we’d have a time complexity of O(n).
'''