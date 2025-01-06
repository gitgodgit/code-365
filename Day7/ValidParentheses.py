class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            char = s[i]
            if char == '{' or char == '[' or char == '(':
                stack.append(char)
            elif char == '}':
                if not stack or stack.pop() != '{':
                    return False
            elif char == ']':
                if not stack or stack.pop() != '[':
                    return False
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        if stack:
            return False
        else:
            return True
        