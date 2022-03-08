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
                rbSum = accMat[i+k if i+k < len(mat) else len(
                    mat) - 1][j+k if j+k < len(mat[0]) else len(mat[0]) - 1]
                rtSum = accMat[i-k-1][j +
                                      k if j+k < len(mat[0]) else len(mat[0]) - 1] if i-k-1 >= 0 else 0
                lbSum = accMat[i+k if i+k <
                               len(mat) else len(mat) - 1][j-k-1] if j-k-1 >= 0 else 0
                ltSum = accMat[i-k-1][j-k-1] if i - \
                    k-1 >= 0 and j-k-1 >= 0 else 0
                answer[i].append(rbSum - rtSum - lbSum + ltSum)
        return answer


# print(Solution().createAccMat([[1, 2], [1, 2]]))
# print(Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1))

assert Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 1) == [
    [12, 21, 16], [27, 45, 33], [24, 39, 28]]
assert Solution().matrixBlockSum([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 2) == [
    [45, 45, 45], [45, 45, 45], [45, 45, 45]]

print('done')
