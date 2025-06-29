class Solution:
    def minLength(self, s: str) -> int:
        stack = []
        for char in s:
            if stack:
                pair = stack[-1] + char
                if pair == "AB" or pair == "CD":
                    stack.pop()
                    continue
            stack.append(char)
        return len(stack)
        