class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = []
        for i in range(m):
            nums3.append(nums1[i])

        n1p, n2p, n3p = 0, 0, 0
        iteration = 0

        print(f"length of nums2 - 1: {len(nums2) - 1} | length of nums3 - 1: {len(nums3) - 1}")
        while n2p < (len(nums2)) and n3p < (len(nums3)):
            print(f"Iteration: {iteration}")
            print(f"n2p: {n2p}")
            print(f"n3p: {n3p}")
            if nums3[n3p] < nums2[n2p]:
                nums1[n1p] = nums3[n3p]
                n3p += 1
                n1p += 1
            else:
                nums1[n1p] = nums2[n2p]
                n2p += 1
                n1p += 1
            iteration += 1

            
        while n2p < len(nums2):
            nums1[n1p] = nums2[n2p]
            n2p += 1
            n1p += 1
        while n3p < len(nums3):
            nums1[n1p] = nums3[n3p]
            n3p += 1
            n1p += 1
        