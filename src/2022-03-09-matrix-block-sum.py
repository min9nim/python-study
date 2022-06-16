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
assert Solution().matrixBlockSum([[1, 1, 1, 1], [1, 1, 1, 1]], 2) == [
    [6, 8, 8, 6], [6, 8, 8, 6]
]


print('done')


'''
ex)
mat: [[1, 1, 1, 1], [1, 1, 1, 1]]
k: 2
answer) [6, 8, 8, 6], [6, 8, 8, 6]



질문1) 제안하신 Brute force 방법의 시간복잡도는? (m,n,k 로 표현)


Hint)
Create a cumulative sum matrix where sum[i][j] is the sum of all cells in the rectangle from (0,0) to (i,j). And use inclusion-exclusion idea.
'''
