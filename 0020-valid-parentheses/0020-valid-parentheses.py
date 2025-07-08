class Solution:
    def isValid(self, s: str) -> bool:

        # stack = []

        # mapping = {")" : "(", "}":"{", "]":"["}

        # for char in s:
        #     if char in mapping:
        #         top_element = stack.pop() if stack else "#"

        #         if mapping[char] != top_element:
        #             return False
            
        #     else:
        #         stack.append(char)

        # return not stack

        # Time Complexity: O(n)
        # Space Complexity: O(n)


                
        # while "()" in s or "{}" in s or '[]' in s:
        #     s = s.replace("()", "").replace('{}', "").replace('[]', "")
        # return s == ''

        # Time Complexity: O(n2)
        # Space Complexity: O(n)



        # openBracket = "({["
        # closeBracket = ")}]"

        # matching = {")":"(", "}":"{", "]":"["}

        # stack = []
        # for char in s:
        #     if char in openBracket:
        #         stack.append(char)
        #     elif char in closeBracket:
        #         if len(stack) == 0:
        #             return False
                
        #         if stack[-1] == matching[char]:
        #             stack.pop()
        #         else:
        #             return False
        # return len(stack) == 0

        # Time Complexity: O(n2)
        # Space Complexity: O(n)


        # stack = []
        # closeToOpen = {")" : "(", "}" : "{", "]" : "["}

        # for c in s:
        #     if  c in closeToOpen:
        #         if stack and stack[-1] == closeToOpen[c]:
        #             stack.pop()
                    
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        # return True if not stack else False

        sk = []
        map_pa = {'(':')', '{':'}', '[':']'}

        for c in s:
            if c in map_pa:
                sk.append(c)
            elif sk and c == map_pa[sk[-1]]:
                sk.pop()
            else:
                return False
        return not sk