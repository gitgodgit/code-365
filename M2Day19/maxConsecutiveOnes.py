def findMaxConsecutiveOnes(nums: list[int]) -> int:
    current = 0
    max_ones = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            max_ones = max(max_ones, current)
            current = 0
        else:
            current += 1
    return max(max_ones, current)