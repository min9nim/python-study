
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


class Solution2:
    def isIsomorphic(self, s: str, t: str) -> bool:
        stMap = {}
        tsMap = {}

        for a, b in zip(s, t):
            if a not in stMap:
                stMap[a] = b
            if b not in tsMap:
                tsMap[b] = a

            if not (stMap[a] == b and tsMap[b] == a):
                return False

        return True


assert Solution2().isIsomorphic('a', 'b') == True
assert Solution2().isIsomorphic('add', 'egg') == True
assert Solution2().isIsomorphic('foo', 'bar') == False
assert Solution2().isIsomorphic('paper', 'title') == True
assert Solution2().isIsomorphic('badc', 'baba') == False
assert Solution2().isIsomorphic("bbbaaaba", "aaabbbba") == False
assert Solution2().isIsomorphic("egcd", "adfd") == False


class Solution3:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))


assert Solution3().isIsomorphic('a', 'b') == True
assert Solution3().isIsomorphic('add', 'egg') == True
assert Solution3().isIsomorphic('foo', 'bar') == False
assert Solution3().isIsomorphic('paper', 'title') == True
assert Solution3().isIsomorphic('badc', 'baba') == False
assert Solution3().isIsomorphic("bbbaaaba", "aaabbbba") == False
assert Solution3().isIsomorphic("egcd", "adfd") == False


print('success!')
