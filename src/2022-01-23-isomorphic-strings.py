
# https://leetcode.com/problems/isomorphic-strings/


class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = dict()
        t2s = dict()
        for a, b in zip(s, t):
            if a == b:
                s2t[a] = b
                t2s[b] = a
                continue
            elif s2t.get(a) == None:
                if t2s.get(b) == None:
                    s2t[a] = b
                    continue
                else:
                    return False
            elif s2t.get(a) == b:
                continue
            else:
                # print(map, a, b)
                return False
        return True


assert Solution().isIsomorphic('a', 'b') == True
assert Solution().isIsomorphic('add', 'egg') == True
assert Solution().isIsomorphic('foo', 'bar') == False
assert Solution().isIsomorphic('paper', 'title') == True
assert Solution().isIsomorphic('badc', 'baba') == False
assert Solution().isIsomorphic("bbbaaaba", "aaabbbba") == False

print('success!')
