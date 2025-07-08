class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        number_from_list = 0
        # Convert the digit list to an int
        for d in digits:
            number_from_list = number_from_list * 10 + d
        number_from_list += 1
        # Convert the updated int back to a list in reverse
        for i in range(len(digits)):
            digits[i] = number_from_list % 10
            number_from_list = number_from_list // 10
        # If there is 1 left over digit at the end, append it
        if number_from_list != 0:
            digits.append(number_from_list)
        digits.reverse() 

        return digits