class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        def sign(x):
            return 1 if x>0 else 0
        stack = []
        for v in asteroids:
            if stack and sign(v) != sign(stack[-1]) and not(sign(v)):
                while stack and sign(v) != sign(stack[-1]) and abs(v)>abs(stack[-1]):
                    stack.pop()
                if not stack or sign(v)==sign(stack[-1]):
                    stack.append(v)
                # if abs(v)<abs(stack[-1]):
                #     continue
                elif abs(v)==abs(stack[-1]):
                    stack.pop()
                    # continue
            else:
                stack.append(v)
        return stack