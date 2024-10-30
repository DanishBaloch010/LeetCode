class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        brackets = {')':'(', '}':'{', ']':'['}
        stack = []
        for char in s:
            # closing bracket
            if char in brackets:
                if stack:
                    top = stack.pop()
                    if top != brackets[char]:
                        return False
            else:
                stack.append(char)

        print(stack)
        return not stack