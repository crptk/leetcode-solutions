class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        x_list = list(x_str)

        x_list.reverse()
        
        if (list(x_str) == x_list):
            return True
        else:
            return False