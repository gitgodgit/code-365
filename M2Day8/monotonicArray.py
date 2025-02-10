def isMonotonic(nums: list[arrays]) -> bool:
    is_increasing = True
    is_decreasing = True
    if len(nums) > 1:
        for i in range(len(nums) - 1):
            if nums[i] <= nums[i+1]:
                is_decreasing = False
            if nums[i] >= nums[i + 1]:
                is_increasing = False
    else:
         return True