class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        distinct = set()

        for num in nums:
            if num in distinct:
                return True
            distinct.add(num)

        return False

'''
Solution by Edrees

This can be easily solved by creating a set, iterating through the list and checking if the number is present in the set. If it isn’t, then add that number to that set. This works because of the properties of a set. A set can only include distinct values and can retrieve values in O(1) time, which makes it the ideal method of solving this problem. Otherwise, you can check if the length of the list converted set is equal to the list, which has the same time/space complexity of O(n).
'''