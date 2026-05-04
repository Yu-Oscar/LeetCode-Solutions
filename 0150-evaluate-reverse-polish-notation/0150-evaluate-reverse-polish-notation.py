class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for token in tokens:
            try: 
                int(token)
                s.append(int(token))
            except ValueError:
                val1 = s.pop()
                val2 = s.pop()
                if token == '+':
                    curr = val2 + val1
                elif token == '-':
                    curr = val2 - val1
                elif token == '*':
                    curr = val2 * val1
                else:
                    curr = int(val2 / val1)
                s.append(curr)

        return s[0]