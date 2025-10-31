class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Create a hash map for the numbers
        numSet = set(nums)
        longest = 0

        for num in numSet:
            # check if its the start of a sequence
            if num-1 not in numSet:
                length = 1
                while num + length in numSet:
                    length +=1 
                
                longest = max(length, longest)
        
        return longest
            
"""
This solution creates a set of the nums list, then iterates through the entire nums list.

    If the number is a starting sequence (that is, the n-1 is in the numSet), then that is we should start
    checking for following numbers

        To check for following numbers, we keep checking if the number has a number to the right of it, basically if n + length is in the list, 
        if it is, we increment:
        length = 0 | n = 5 | nums + length = 5 
        length = 1 | n = 5 | nums + length = 6
        etc.

    Return the max of the now computed length to our longest computed length, and replace it accordingly

Return the longest computed length
"""
    
