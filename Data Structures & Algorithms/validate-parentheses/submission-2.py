class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
             return False
        stack = []
        pair = { '}' : '{', ']' : '[', ')' : '('}

        for c in s:
            if c in pair.values():
                stack.append(c)
            else:
                if stack and (stack[-1] == pair[c]):
                    stack.pop()
                else:
                    return False
        print(stack)
        return stack == []




