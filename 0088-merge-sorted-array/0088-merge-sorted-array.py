class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1[:m]

        # Pointers for each num
        n1p, n2p, n3p = 0, 0, 0
        iteration = 0

        # Overrwriting elements until the end of one array is reached
        while n2p < (len(nums2)) and n3p < (len(nums3)):
            if nums3[n3p] < nums2[n2p]:
                nums1[n1p] = nums3[n3p]
                n3p += 1
                n1p += 1
            else:
                nums1[n1p] = nums2[n2p]
                n2p += 1
                n1p += 1
            iteration += 1

        # If there are any elements left in one of the arrays, append it to nums1
        while n2p < len(nums2):
            nums1[n1p] = nums2[n2p]
            n2p += 1
            n1p += 1
        while n3p < len(nums3):
            nums1[n1p] = nums3[n3p]
            n3p += 1
            n1p += 1
        