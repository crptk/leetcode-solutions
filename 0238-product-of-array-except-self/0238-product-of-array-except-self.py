class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Create empty product arra
        product_nums = [1] * len(nums)

        prefix, postfix = 1, 1

        for i in range(1, len(nums), 1):
            prefix *= nums[i - 1]
            product_nums[i] = prefix

        for j in range(len(nums)-2, -1, -1):
            postfix *= nums[j + 1]
            product_nums[j] *= postfix
        return product_nums