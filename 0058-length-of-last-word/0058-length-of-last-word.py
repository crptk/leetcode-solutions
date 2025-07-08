class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_string = s.split()

        size = len(split_string)

        return len(split_string[size - 1])
