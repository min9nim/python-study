class Solution:
    def addBinary(self, a: str, b: str) -> str:
        aLen, bLen = len(a), len(b)
        if aLen > bLen:
            b = '0' * (aLen-bLen) + b
        else:
            a = '0' * (bLen - aLen) + a
        result = ''

        flag = False
        for i in range(len(a)-1, -1, -1):
            if a[i] == '0' and b[i] == '0':
                if flag:
                    result = '1' + result
                    flag = False
                else:
                    result = '0' + result
            if a[i] != b[i]:
                if flag:
                    result = '0' + result
                else:
                    result = '1' + result
            if a[i] == '1' and b[i] == '1':
                if flag:
                    result = '1' + result
                else:
                    result = '0' + result
                    flag = True
        return '1' + result if flag else result


assert Solution().addBinary('11', '1') == '100'
assert Solution().addBinary('1010', '1011') == '10101'

print('done')
