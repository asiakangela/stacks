class Solution:
    def isValid(self, s :str) -> bool:
        stack = []
        set = {")" : "(", "}" : "{", "]" : "[" }
        for p in s :
            if p in set.values():
                stack.append(p)
            elif stack and set[p] == stack[-1]:
                stack.pop()
            else:
                return False
        return stack == []
