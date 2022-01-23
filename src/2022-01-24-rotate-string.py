# https://leetcode.com/problems/rotate-string/


class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(s)):
            if s[i:] + s[0:i] == goal:
                return True
        return False


assert Solution().rotateString("abcde", "cdeab") == True


class Solution2:
    def rotateString(self, s: str, goal: str) -> bool:
        return len(s) == len(goal) and goal in s+s


assert Solution2().rotateString("abcde", "cdeab") == True


print('success!')
