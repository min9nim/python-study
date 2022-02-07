# https://leetcode.com/problems/long-pressed-name/


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        repeatedStr = ''
        size = len(name)
        for i, v in enumerate(name):
            repeatedStr += v
            if i < size-1 and name[i+1] == v:
                continue
            else:
                if repeatedStr == typed[0:len(repeatedStr)]:
                    typed = typed[len(repeatedStr):]
                    while typed != '' and typed[0] == v:
                        typed = typed[1:]
                    repeatedStr = ''
                else:
                    return False
        return typed == ''


assert Solution().isLongPressedName('alex', 'aaleex') == True
assert Solution().isLongPressedName('saeed', 'ssaaedd') == False
assert Solution().isLongPressedName('keating', 'keat') == False
assert Solution().isLongPressedName('aabbcc', 'aaaabbbbb') == False


class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        i = 0
        for j in range(len(typed)):
            if i < len(name) and name[i] == typed[j]:
                i += 1
            elif i == 0 or name[i - 1] != typed[j]:
                return False
        return i == len(name)


assert Solution().isLongPressedName('alex', 'aaleex') == True
assert Solution().isLongPressedName('saeed', 'ssaaedd') == False
assert Solution().isLongPressedName('keating', 'keat') == False
assert Solution().isLongPressedName('aabbcc', 'aaaabbbbb') == False


print('success!')
