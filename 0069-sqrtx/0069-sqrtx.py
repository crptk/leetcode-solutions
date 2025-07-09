class Solution:
    def mySqrt(self, x: int) -> int:
        i = 0

        flag = True
        while flag:
            if i * i <= x and (i + 1) * (i + 1) > x:
                flag = False
                return i
            i += 1
        
            