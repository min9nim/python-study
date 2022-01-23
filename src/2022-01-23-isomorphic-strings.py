
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMap = dict()
        tMap = dict()
        for i, (a, b) in enumerate(zip(s, t)):
            if sMap.get(a) == None:
                sMap[a] = [i]
            else:
                sMap[a].append(i)
            if tMap.get(b) == None:
                tMap[b] = [i]
            else:
                tMap[b].append(i)
            if sMap[a] != tMap[b]:
                return False
        return True


assert Solution().isIsomorphic('a', 'b') == True
assert Solution().isIsomorphic('add', 'egg') == True
assert Solution().isIsomorphic('foo', 'bar') == False
assert Solution().isIsomorphic('paper', 'title') == True
assert Solution().isIsomorphic('badc', 'baba') == False
assert Solution().isIsomorphic("bbbaaaba", "aaabbbba") == False
assert Solution().isIsomorphic("egcd", "adfd") == False

print('success!')
