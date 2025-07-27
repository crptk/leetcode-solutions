class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # [[], [], [], ..., []]

        for n in nums:
            count[n] = 1 + count.get(n, 0) # add 1 to it if it has an element, else default to 0 and add 1
        for n, c in count.items():
            freq[c].append(n) # Append at the count index which number appeared that many times
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # For each number that is in the current frequency index (skip if empty [])
                res.append(n)
                if len(res) == k:
                    return res # Guaranted to execute

'''
Solved by Edrees

This solution uses bucket sort with a time complexity of O(n) time. We first start with a hash map containing the frequencies of each number.
After that, create a list of empty lists "freq" that are the same size as the given "nums" list. We then append to this frequency at the count index,
which number appeared that many times ("count" times). Then we traverse from right to left of "freq" (from most freq to least freq), returning the first 
k values that we encounter. 
'''            