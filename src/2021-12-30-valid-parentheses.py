class Solution:
    def isValid(self, s: str) -> bool:
        map = {")": "(", "}": "{", "]":"["}
        stack = []
        for i in range(len(s)) :
            if s[i] in ['(', '{', '['] :
                stack.append(s[i])
            elif len(stack) > 0 and stack[-1] == map[s[i]] :
                stack.pop()
            else :
                return False
        return len(stack) == 0


s = Solution()

print(s.isValid("()"))
