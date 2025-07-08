class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Pointers to keep track of each binary string
        i = len(a) - 1
        j = len(b) - 1
        carry = 0  # Carry variable to use in the operation
        result = [] # Variable to append final result to

        '''
        While we haven't reached an end to either binary,
        or the carry is still there, keep looping
        '''
        while i >= 0 or j >= 0 or carry > 0:
            '''
            If there are still numbers in either bit string to loop through,
            then set it to the current bit the pointer is on, else 0
            '''
            bit_a = int(a[i]) if i >= 0 else 0
            bit_b = int(b[j]) if j >= 0 else 0

            # Adding the current bit, and appending to the resulting variable
            total = bit_a + bit_b + carry # This will either be 0, 1, 2, or 3
            result.append(str(total % 2)) # Modular 2 to get either a 1 or 0

            # Checking if there is a remainder in the total, if it's 2 or 3, it'll
            # mean that there is a carry to the next number
            carry = total // 2

            # Subtract pointers to allow for right to left iteration
            i -= 1
            j -= 1

        # Reverse the resulting array since we were working from right to left
        result.reverse()

        # Convert the int array to a string and return it
        return ''.join(result)