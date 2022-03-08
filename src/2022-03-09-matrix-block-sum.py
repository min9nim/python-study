# https://leetcode.com/problems/matrix-block-sum/

from typing import List


class Solution:
    def createAccMat(self,  mat: List[List[int]]):
        result = []
        for i in range(len(mat)):
            accSum = 0
            result.append([])
            for j in range(len(mat[0])):
                accSum += mat[i][j]
                result[i].append((result[i-1][j] if i-1 >= 0 else 0) + accSum)
        return result

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        accMat = self.createAccMat(mat)
        answer = []
        for i in range(len(mat)):
            answer.append([])
            for j in range(len(mat[0])):
                rx = i+k if i+k < len(mat) else len(mat) - 1
                ry = j+k if j+k < len(mat[0]) else len(mat[0]) - 1
                lx = i-k if i-k > 0 else 0
                ly = j-k if j-k > 0 else 0
                answer[i].append(accMat[rx][ry]
                                 - (accMat[rx][ly-1] if ly-1 >= 0 else 0)
                                 - (accMat[lx-1][ry] if lx-1 >= 0 else 0)
                                 + (accMat[lx-1][ly-1]
                                    if lx - 1 >= 0 and ly-1 >= 0 else 0)
                                 )
        return answer


# print(Solution().createAccMat([[1, 2], [1, 2]]))
# print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))

assert Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [
    [12, 21, 16], [27, 45, 33], [24, 39, 28]]
assert Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [
    [45, 45, 45], [45, 45, 45], [45, 45, 45]]

print('done')
