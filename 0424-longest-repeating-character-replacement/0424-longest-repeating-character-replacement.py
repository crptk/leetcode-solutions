class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0
        max_freq = 0
        count = {}
        l = 0

        for r in range(len(s)):
            count[s[r]] = count.get(s[r], 0) + 1
            max_freq = max(max_freq, count[s[r]])
            while (r - l + 1) - max_freq > k:
                count[s[l]] -= 1
                l += 1

            max_len = max(max_len, r - l + 1)
        return max_len


'''
Solution by Edrees

This solution consists of a sliding window approach where we keep track of the frequency
of each character within our window after each iteration, if the unique characters within
the window exceed the amount of unique characters allowed (k), then we keep incrementing the left
pointer accordingly. Keep updating the frequency as the left pointer is being updated, and update
the max length with the current length of the window

Time complexity: O(n)
Space complexity: O(m)
'''