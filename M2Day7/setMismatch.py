def findErrorNums(nums: list[int]) -> list[int]:
    missing = 0
    repeated = 0
    for i in range(1, len(nums) ):
        if i + 1 not in nums:
            missing = i + 1
        if nums.count(i + 1) == 2:
            repeated = i
    return [repeated, missing]

