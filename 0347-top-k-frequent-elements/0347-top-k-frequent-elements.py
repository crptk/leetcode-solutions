class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            else:
                hashmap[num] = 1
        sorted_items = sorted(hashmap.items(), key=lambda x: x[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]

