class Solution:
    def isValid(self, str):
        stack = []
        self.str = str
        for char in str:
            if char == '{':
                stack.append('{')
            elif char == '[':
                stack.append('[')
            elif char == '(':
                stack.append('(')
            else:
                if stack == []:
                    return False
                if char == '}' and stack[-1] == '{':
                    stack.pop()
                elif char == ']' and stack[-1] == '[':
                    stack.pop()
                elif char == ')' and stack[-1] == '(':
                    stack.pop()
                else:
                    return False
        return stack == []
        