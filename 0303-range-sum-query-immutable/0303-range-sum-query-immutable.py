class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = [0]
        for n in nums:
            self.prefixes.append(self.prefixes[-1] + n)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right + 1] - self.prefixes[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


'''
Written by Edrees

Prefixes in python are used to get the sum of an index at an array of all the numbers before it and including. So if I had a list of [1,2,3,4,5,6], with a prefix at index 3, it would be [1 + 2 + 3 + 4] = [10], which would be the value stored in the prefix.

Now for the problem, I first initialized the prefixes variable with [0], this is so I can have a variable/prefix to append to in the loop. Afterwards, I appended to the prefixes variable by adding the current value at index n for nums onto the current sum of all numbers (the last value in prefixes), then appending that to prefixes. This would result in an array [1,2,3,4,5,6] with a prefixes variable of [0,1,3,6,10,15,21] for example. 

Now in the sumRange, we need to get the sum of the numbers between the left and right index for the list ‘nums’. To do this, we can simply get the index at right + 1 in the prefixes variable, then cut off all the ones before index left by subtracting the index at left for the prefixes variable. What results is the sum of the range between left and right in variable ‘nums’. The reason we start at right + 1 is because we initialized 0 for prefixes in the beginning, so we need to shift everything to the right by 1. Otherwise it would be prefixes[right] - prefixes[left - 1]
'''