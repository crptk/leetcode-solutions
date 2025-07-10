class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place, assuming nums1 has enough space.
        """
        # Copy the first m elements of nums1
        nums1_copy = nums1[:m]

        # Initialize pointers
        p1 = p2 = p = 0

        # Merge until one list is exhausted
        while p1 < m and p2 < n:
            if nums1_copy[p1] < nums2[p2]:
                nums1[p] = nums1_copy[p1]
                p1 += 1
            else:
                nums1[p] = nums2[p2]
                p2 += 1
            p += 1

        # Append remaining elements
        if p1 < m:
            nums1[p:m + n] = nums1_copy[p1:]
        if p2 < n:
            nums1[p:m + n] = nums2[p2:]
