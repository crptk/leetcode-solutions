class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = '+-*/'

        for token in tokens:
            if token in operators:
                num1 = stack.pop()
                num2 = stack.pop()

                if token == '*':
                    stack.append(num2 * num1)
                elif token == '+':
                    stack.append(num2 + num1)
                elif token == '-':
                    stack.append(num2 - num1)
                elif token == '/':
                    stack.append(int(num2 / num1))
            else:
                stack.append(int(token))

        return stack[-1]

"""
Solution by Edrees

This solution involves using a stack to detect if there is an operand or number

If there is a number:
- append it to the stack. 

If it's an operand:
- use the operand on the last two numbers of the stack.
- store this in res
- append res to stack

return the last element of res

This ensures that we always operate on the last two numbers, and that the last number of the stack
will always contain the final result.
"""