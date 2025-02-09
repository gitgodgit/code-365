def isMonotonic(nums: list[arrays]) -> bool:
    is_true = True
    if len(nums) > 1:
        if nums[0] <= nums[len(nums) - 1]
            for i in range(len(nums) - 1):
                if nums[i+1] >= nums[i]:
                    continue
                else:
                    is_true = False
        else:
           for i in range(len(nums) - 1):
               if nums[i+1] <= nums[i]:
                   continue
                else:
                    is_true = False
     else:
         return True