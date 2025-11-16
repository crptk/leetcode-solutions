class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening_characters = '({['
        closing_characters = ')}]'

        bracket_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }
        for char in s:
            if char in opening_characters:
                stack.append(char)
            elif char in closing_characters:
                if not stack or bracket_dict[char] != stack[-1]:
                    return False
                stack.pop()
            else:
                continue
        return len(stack) == 0

'''
Solution by Crptk

We basically keep storing the open brackets into a stack, and then as soon as we run into a closing
bracket, we check if it corresponds to the top element of the stack (the last seen opening bracket) and 
if it doesn't we return False. Keep doing this until we traverse the entire string, and return True if 
the stack is empty, False if otherwise. This prevents unclosed open parantheses
'''