class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def helper(op,lst):
            res = lst.pop()
            if op == '&':
                for val in lst:
                    res = res & val
            elif op == '|':
                for val in lst:
                    res |= val
            else:
                res = not(res)
            return 't' if res else 'f'
        stack = []
        for ex in expression:
            if ex == ')':
                lst = []
                while stack[-1] != '(':
                    lst.append(True if stack.pop()=='t' else False)
                stack.pop()
                stack.append(helper(stack.pop(), lst))
            else:
                if ex == ',': continue
                stack.append(ex)
        # print(stack)
        return True if stack[0]=='t' else False