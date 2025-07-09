class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        first = 1  # ways to climb 1 step
        second = 2  # ways to climb 2 steps

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third
        
        return second

        