class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for br in s:
            if br == ')':
                if stack and stack[-1]=='(':
                    stack.pop()
                else:
                    stack.append(')')
            else:
                stack.append('(')
        return len(stack)