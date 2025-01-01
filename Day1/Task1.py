nums = [2,7,11,15]
target = 9
nums2 = [3,2,4]
target2 = 6
def twoSum(nums, target):
    for i in range(len(nums) -1):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                indexes = [i , j]
                return indexes
    

print(twoSum(nums, target))
print(twoSum(nums2, target2))
