
def solution(nums, k):
    acc = []
    sum = 0
    m = len(nums)
    for n in nums:
        sum += n
        acc.append(sum)

    answer = []
    for i in range(m):
        answer.append((acc[i+k] if i+k < m else acc[m-1]) -
                      (acc[i-k-1] if i-k-1 >= 0 else 0))

    return answer


assert solution([1, 1, 1, 1, 1], 2) == [3, 4, 5, 4, 3]
assert solution([1, 2, 3, 4, 5], 1) == [3, 6, 9, 12, 9]
assert solution([2, 3, 3, 3, 1], 9) == [12, 12, 12, 12, 12]
assert solution([2, 3, 3, 3, 1], 4) == [12, 12, 12, 12, 12]
assert solution([2, 3, 3, 3, 1], 1) == [5, 8, 9, 7, 4]
assert solution([3], 9) == [3]
assert solution([1, -1, 0, 1, -1], 1) == [0, 0, 0, 0, 0]
