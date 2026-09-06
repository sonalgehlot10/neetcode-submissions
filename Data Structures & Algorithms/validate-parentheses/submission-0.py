class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closePToOpenP = {
            '}':'{',
            ']':'[',
            ')':'('
        }

        for c in s:
            if c not in closePToOpenP:
                stack.append(c)
            else:
                if stack and stack[-1]==closePToOpenP[c]:
                    stack.pop()
                else:
                    return False
        
        if not stack:
            return True
        return False
