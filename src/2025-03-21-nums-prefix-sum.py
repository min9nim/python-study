def solution(nums, k):
    m = len(nums)

    acc = []
    for i in range(m):
        acc.append(nums[i] + (acc[i-1] if i-1 >= 0 else 0))
    
    answer = []
    for i in range(m):
        answer.append(acc[i+k if i+k < m else m-1] - (acc[i-k-1] if i-k-1 >= 0 else 0))
        
    return answer


assert solution([1, 2, 3], 1) == [3,6,5]
assert solution([1, 1,1,1,1], 2) == [3,4,5,4,3]
assert solution([1, 2, 3, 4, 5], 2) == [6,10,15,14,12]
assert solution([1, 2, 3, 4, 5], 1) == [3,6,9,12,9]


print('done')
