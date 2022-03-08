# https://leetcode.com/problems/matrix-block-sum/

from typing import List


class Solution:

    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        accMat = []
        for i in range(m):
            accSum = 0
            accMat.append([])
            for j in range(n):
                accSum += mat[i][j]
                accMat[i].append((accMat[i-1][j] if i-1 >= 0 else 0) + accSum)

        answer = []
        for i in range(m):
            answer.append([])
            for j in range(n):
                rx = min(i+k, m - 1)
                ry = min(j+k, n - 1)
                lx = max(i-k, 0)
                ly = max(j-k, 0)
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
